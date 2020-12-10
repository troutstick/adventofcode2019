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

pub fn intcode_computer(prog_ref: &Vec<usize>, noun: usize, verb: usize) -> usize {

    let mut program = prog_ref.clone();

    let mut ptr = 0;
    program[1] = noun;
    program[2] = verb;
    loop {
        match program[ptr] {
            1 => {
                // add
                let pos1 = program[ptr + 1];
                let pos2 = program[ptr + 2];
                let pos3 = program[ptr + 3];
                program[pos3] = program[pos1] + program[pos2];
                ptr += 4;
            },
            2 => {
                // multiply
                let pos1 = program[ptr + 1];
                let pos2 = program[ptr + 2];
                let pos3 = program[ptr + 3];
                program[pos3] = program[pos1] * program[pos2];
                ptr += 4;
            },
            99 => break,
            _ => panic!("Encountered illegal opcode"),
        }
    }
    
    program[0]

}