import pytest


@pytest.mark.usefixtures("init")
def test_basic_contract(protostar):
    result = protostar(["test", "tests"])
    assert "1 passed" in result


@pytest.mark.usefixtures("init")
def test_complex(protostar, copy_fixture):
    copy_fixture("basic.cairo", "./src")
    copy_fixture("proxy_contract.cairo", "./src")
    copy_fixture("test_proxy.cairo", "./tests")

    result = protostar(["test", "tests"])

    assert "Collected 3 items" in result
    assert "3 passed" in result


@pytest.mark.usefixtures("init")
def test_expect_revert(protostar, copy_fixture):
    copy_fixture("test_expect_revert.cairo", "./tests")

    result = protostar(["test", "tests"])
    print(result)

    assert "Collected 10 items" in result
    assert "5 passed" in result
    assert "5 failed" in result
    assert "test_expect_revert.cairo::test_with_except_revert_fail_expected" in result
    assert (
        "test_expect_revert.cairo::test_with_except_out_of_scope_revert_fail_expected"
        in result
    )
    assert (
        "test_expect_revert.cairo::test_call_not_existing_contract_fail_expected"
        in result
    )
    assert (
        "test_expect_revert.cairo::test_error_was_not_raised_before_stopping_expect_revert_fail_expected"
        in result
    )
    assert "name: RANDOM_ERROR_NAME, message:" in result
