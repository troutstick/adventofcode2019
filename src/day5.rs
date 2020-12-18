use super::utils::*;

pub fn solve(input: &str) {
    println!("Doing day 5");
    let program = gen_program(input);
    intcode_computer(&program, program[0], program[1]);
}

#[test]
fn day5test() {
    let program = vec![3,0,4,0,99];
    intcode_computer(&program, 3, 0);
}