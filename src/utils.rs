use std::io;

pub fn intcode_computer(prog_ref: &Vec<isize>, noun: isize, verb: isize) -> isize {

    let mut program = prog_ref.clone();

    let mut ptr = 0;
    program[1] = noun;
    program[2] = verb;
    loop {
        let mut instruction = program[ptr];
        let opcode = instruction % 100;
        instruction /= 100;
        let mode1 = instruction % 10;
        instruction /= 10;
        let mode2 = instruction % 10;
        instruction /= 10;
        let mode3 = instruction % 10;

        let decode = |param, mode| -> isize {
            match mode as usize {
                0 => program[param as usize],
                1 => param,
                _ => panic!("Given illegal program parameter!"),
            }
        };

        match opcode {
            1 => {
                // add
                let pos1 = program[ptr + 1];
                let pos2 = program[ptr + 2];
                let pos3 = program[ptr + 3] as usize;
                program[pos3] = decode(pos1, mode1) + decode(pos2, mode2);
                ptr += 4;
            },
            2 => {
                // multiply
                let pos1 = program[ptr + 1];
                let pos2 = program[ptr + 2];
                let pos3 = program[ptr + 3] as usize;
                program[pos3] = decode(pos1, mode1) * decode(pos2, mode2);
                ptr += 4;
            },
            3 => {
                let mut input = String::new();
                println!("Requesting user input: ");
                io::stdin().read_line(&mut input).expect("Failed to read input");
                println!("Received input: `{}`", input.trim());
                let input = input.trim().parse::<isize>().unwrap();

                let pos = program[ptr + 1] as usize;
                program[pos] = input;
                ptr += 2;
            },
            4 => {
                let pos = program[ptr + 1] as usize;
                println!("Program output: `{}`", program[pos]);
                ptr += 2;
            },
            99 => break,
            _ => panic!("Encountered illegal opcode"),
        }
    }
    
    program[0]

}

pub fn gen_program(input: &str) -> Vec<isize> {
    input
        .split(",").map(|s| s.trim())
        .filter(|s| !s.is_empty())
        .map(|s| s.parse().unwrap())
        .collect()
}