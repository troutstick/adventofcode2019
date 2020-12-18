use super::utils::*;

pub fn solve(input: &str) {
    println!("Doing day 2");
    let program = gen_program(input);
    
    println!("The answer to day 2 part 1 is {}", intcode_computer(&program, 12, 2));
    
    for i in 0..100 {
        for j in 0..100 {
            let output = intcode_computer(&program, i, j);
            if output == 19690720 {
                println!("The answer to day 2 part 2 is {}", 100*i+j);
                return;
            }
        }
    }
}