# Muhammad Ahmad, CMS 542432, BSCS-15-D
import unittest

from evaluate import citation_correct, is_refusal, parse_letter


class ParserTests(unittest.TestCase):
    def check_cases(self, cases, parser):
        for name, value, expected in cases:
            with self.subTest(name=name):
                actual = parser(value)
                print(f"{'PASS' if actual == expected else 'FAIL'}: {name}")
                self.assertEqual(actual, expected, f"{name}: expected {expected!r}, got {actual!r}")

    def test_mcq_letters(self):
        cases = [
            ("answer colon", "Answer: C", "C"),
            ("answer is", "Answer is B", "B"),
            ("choice label", "Choice D", "D"),
            ("option label", "Option A", "A"),
            ("lowercase answer", "answer: b", "B"),
            ("first line closing parenthesis", "C)\nBecause it is correct", "C"),
            ("first line period", "D. Correct", "D"),
            ("first line lone letter", "A\nExplanation follows", "A"),
            ("first line trailing whitespace", "B   \nExplanation follows", "B"),
            ("parenthesized first line", "(B)\nExplanation follows", "B"),
            ("leading article is not an answer", "A statute sets out the rule.", None),
            ("unlabeled prose is not an answer", "The correct option is C.", None),
            ("several explicit letters", "Answer: A; Option C", None),
            ("several alternatives", "Answer: A or B", None),
            ("period-separated alternatives", "Answer: A. B.", None),
            ("answer with another letter", "Answer: A, but B is incorrect.", None),
            ("conflicting first line and label", "A)\nAnswer: B", None),
            ("unknown option", "Answer: E", None),
        ]
        self.check_cases(cases, parse_letter)

    def test_citations(self):
        cases = [
            ("constitution article", ("Constitution Article 19", "constitution", "19"), True),
            ("penal code section", ("PPC Section 302", "ppc", "302"), True),
            ("named penal code", ("Section 302 of the Pakistan Penal Code", "ppc", "302"), True),
            ("PECA section", ("PECA Section 11", "peca", "11"), True),
            ("electronic crimes name", ("Section 11 Prevention of Electronic Crimes Act", "peca", "11"), True),
            ("alphanumeric suffix", ("PPC Section 153A", "ppc", "153-A"), True),
            ("hyphenated suffix", ("PPC s. 175-A", "ppc", "175A"), True),
            ("hyphenated number suffix", ("PPC Section 489-F", "ppc", "489F"), True),
            ("article abbreviation", ("Constitution Art. 19", "constitution", "19"), True),
            ("section abbreviation", ("Penal Code s. 302", "ppc", "302"), True),
            ("wrong number", ("PECA Section 12", "peca", "11"), False),
            ("law too far away", ("PPC " + ("x" * 41) + " Section 302", "ppc", "302"), False),
            ("number without cue", ("PPC 302", "ppc", "302"), False),
            ("number before cue", ("302 under PPC Section 12", "ppc", "302"), False),
            ("number too far from law", ("PPC " + ("x" * 41) + " Section 302", "ppc", "302"), False),
            ("law and number within 40 chars", ("PPC " + (" " * 31) + "Section 302", "ppc", "302"), True),
            ("cue text counts toward distance", ("PPC " + (" " * 32) + "Section 302", "ppc", "302"), False),
        ]
        for name, (answer, law, number), expected in cases:
            with self.subTest(name=name):
                actual = citation_correct(answer, law, number)
                print(f"{'PASS' if actual == expected else 'FAIL'}: {name}")
                self.assertEqual(actual, expected, f"{name}: expected {expected!r}, got {actual!r}")

    def test_refusals(self):
        configured = "I don't know - this is not in the provided text."
        cases = [
            ("configured refusal", configured, True),
            ("case insensitive", "I DON'T KNOW.", True),
            ("curly apostrophe", "I don’t know.", True),
            ("provided context", "This is not in the provided context.", True),
            ("provided text", "Not in the provided text.", True),
            ("answer absent from provided context", "The answer is not in the provided context.", True),
            ("cannot determine", "I cannot determine the answer.", True),
            ("unable to determine", "Unable to determine from context.", True),
            ("insufficient context", "Insufficient context to answer.", True),
            ("refusal in first 250 chars", "I don't know. " + ("x" * 300), False),
            ("answer after first 250 chars", configured + (" " * 300) + "The rule is different.", False),
            ("this is not in context", "This is not in the provided context.", True),
            ("refusal followed by answer", "I don't know, but Section 302 says this is prohibited.", False),
            ("refusal followed by citation", "I don't know. PPC Section 302.", False),
            ("substantive answer before refusal", "Section 302 applies. I don't know.", False),
            ("unrecognized hedging", "Maybe I could not determine it.", False),
            ("non-refusal answer", "PPC Section 302 provides the rule.", False),
        ]
        for name, answer, expected in cases:
            with self.subTest(name=name):
                actual = is_refusal(answer, configured)
                print(f"{'PASS' if actual == expected else 'FAIL'}: {name}")
                self.assertEqual(actual, expected, f"{name}: expected {expected!r}, got {actual!r}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
