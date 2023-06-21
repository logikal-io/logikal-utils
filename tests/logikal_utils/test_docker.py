from pytest import raises
from pytest_mock import MockerFixture

from logikal_utils import docker


def test_non_existent_service(mocker: MockerFixture) -> None:
    run = mocker.patch('logikal_utils.docker.subprocess.run')
    with raises(RuntimeError, match='service .* not found'):
        docker.Service(name='non-existent')
    assert run.called


def test_unhealthy(mocker: MockerFixture) -> None:
    attrs = {'State': {'Health': {'Status': 'unhealthy'}}}
    client = mocker.patch('logikal_utils.docker.client_from_env').return_value
    client.containers.list.return_value = [mocker.Mock(attrs=attrs)]
    with raises(RuntimeError, match='service .* is not healthy'):
        docker.Service(name='mock')


def test_ready_log_text(mocker: MockerFixture) -> None:
    ready_log_text = 'service is ready'
    run = mocker.patch('logikal_utils.docker.subprocess.run')
    client = mocker.patch('logikal_utils.docker.client_from_env').return_value
    container = mocker.Mock(attrs={'State': {'Health': {'Status': 'healthy'}}})

    # Not ready
    client.containers.list.side_effect = [[], [container]]
    container.logs.return_value = b'client log'
    with raises(RuntimeError, match='service .* is not ready'):
        docker.Service(
            name='mock', ready_log_text=ready_log_text,
            start_timeout_seconds=0.1, log_poll_seconds=0.1,
        )
    assert run.called

    # Ready
    sleep = mocker.patch('logikal_utils.docker.sleep')
    client.containers.list.side_effect = [[], [container]]
    container.logs.return_value = ready_log_text.encode()
    docker.Service(name='mock', ready_log_text=ready_log_text)
    assert not sleep.called


def test_container_port() -> None:
    assert docker.Service(name='validator').container_port(service_port='8888/tcp') != '0'
