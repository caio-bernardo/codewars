/* String ends with?
* Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
* */

fn ends_with(word: &str, ending: &str) -> bool {
    if word.len() < ending.len() {
        return false;
    }
    &word[word.len() - ending.len()..] == ending
}

fn main() {
    dbg!(ends_with("abc", "c"));
    dbg!(ends_with("strawberry", "banana"));
    dbg!(ends_with("a", "bc"));
}
