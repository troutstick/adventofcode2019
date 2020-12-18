use super::utils::intcode_computer;

pub fn solve(input: &str) {
    println!("Doing day 2");
    let program: Vec<usize> = input
        .split(",").map(|s| s.trim())
        .filter(|s| !s.is_empty())
        .map(|s| s.parse().unwrap())
        .collect();
    
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