from .. import hello


def test_main(capsys):
    hello.main(["Shaheer"])

    out, err = capsys.readouterr()
    assert out == "Hello Person Shaheer\n"
    assert err == ""


def test_main_error_with_empty_str(capsys):
    assert hello.main([""])

    out, err = capsys.readouterr()
    assert out == ""
    assert err == "Person's name must not be empty!\n"
