from pytest import Pytester

pytest_plugins = ['pytester']


def test_hide_traceback(pytester: Pytester) -> None:
    pytester.makepyfile("""
        from logikal_utils.testing import hide_traceback

        @hide_traceback
        def assertion_error() -> None:
            raise AssertionError('Error')

        def test_hide_traceback() -> None:
            assertion_error()

    """)
    result = pytester.runpytest('--live', '--fast')
    result.stdout.re_match_lines([
        'E +AssertionError: Error.*',
        'All traceback entries are hidden..*',
    ])
    result.stdout.no_re_match_line(r'.*value_error\(\).*')
    result.stdout.no_re_match_line('.*raise ValueError.*')


def test_hide_traceback_other_error(pytester: Pytester) -> None:
    pytester.makepyfile("""
        from logikal_utils.testing import hide_traceback

        @hide_traceback
        def value_error() -> None:
            raise ValueError('Error')

        def test_hide_traceback_other_error() -> None:
            value_error()

    """)
    result = pytester.runpytest('--live', '--fast')
    result.stdout.re_match_lines([
        r'> +value_error\(\).*',
        r' +def value_error\(\).*',
        r'> +raise ValueError\(\'Error\'\).*',
        'E +ValueError: Error.*',
    ])
