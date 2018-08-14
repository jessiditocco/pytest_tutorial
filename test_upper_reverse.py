def upper_reverse(text):
	return "".join(reversed(text.upper()))


def test_upper_reverse():
		assert upper_reverse("hello") == "OLLEH"


# with pytest, we can use assertions with plain assert statment
# subclassing TestCase is not reuqired
# Tests are found and collected with the py.test command 