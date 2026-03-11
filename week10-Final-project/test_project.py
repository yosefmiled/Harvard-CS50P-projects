from project import get_african_countries, validate, prompt, format_response

def test_get_african_countries():
    countries = get_african_countries()
    assert len(countries) == 54
    for country in countries :
        assert len(country) == 3
def test_get_african_countries_has_tunisia():
    names = [c[0] for c in get_african_countries()]
    assert "Tunisia" in names

def test_validate():
    assert validate("1", 54) == True
    assert validate("54", 54) == True
    assert validate("4", 4) == True
def test_validate_NotValid():
    assert validate("0", 54) == False
    assert validate("55", 54) == False
    assert validate(" ", 54) == False
    assert validate("abcd", 54) == False

def test_prompt():
    result = prompt("Tunisia", "History", "Ancient History")
    assert "Tunisia" in result
    result = prompt("Ghana", "History", "Something Unknown")
    assert "Ghana" in result
def test_prompt_returns_string():
    result = prompt("Nigeria", "Food & Recipes", "National Dishes")
    assert isinstance(result, str)
    assert len(result) > 0

def test_format_response():
    assert format_response("") == ""
    assert format_response("            helloooo     ") == "helloooo"
def test_format_response_blank_lines():
    text= "Hello " \
    "" \
    "" \
    "" \
    "World"
    result = format_response(text)
    assert "\n\n" not in result
    assert "Hello" in result
    assert "World" in result


