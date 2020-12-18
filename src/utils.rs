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