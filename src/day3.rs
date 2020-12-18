use std::{cmp::min, collections::hash_map::*};

#[derive(PartialEq, Eq, Hash, Clone)]
struct Position {
    x: isize,
    y: isize,
}

pub fn solve(input: &str) {
    println!("Doing day 3");
    let wires: Vec<&str> = input.split_whitespace().collect();
    
    let wire0_map = init_wire(wires[0]);

    closest_to_center(wires[1], wire0_map); 
}

fn closest_to_center(dir_str: &str, wire0: HashMap<Position, isize>) {
    let directions = dir_str.split(",").map(|s| s.trim());
    let mut x = 0;
    let mut y = 0;

    let mut distance = 0;

    let mut min_manhattan = isize::MAX;
    let mut min_sig_delay = isize::MAX;

    let mut skipped_first = false;

    for dir in directions {
        let mut dir_chars = dir.chars();
        let (x_inc, y_inc) = incrementor(dir_chars.next().unwrap()); // parse direction
        let mut section_len = dir_chars.collect::<String>().parse::<isize>().unwrap();

        while section_len > 0 {
            if skipped_first {
                let pos = Position{x,y};
                if wire0.contains_key(&pos) {
                    min_manhattan = min(x.abs()+y.abs(), min_manhattan);
                    min_sig_delay = min(wire0.get(&pos).unwrap() + distance, min_sig_delay);
                }
            } else {
                skipped_first = true;
            }
            x += x_inc;
            y += y_inc;
            section_len -= 1;
            distance += 1;
        }
    }
    let pos = Position{x,y};
    if wire0.contains_key(&pos) {
        min_manhattan = min(x.abs()+y.abs(), min_manhattan);
        min_sig_delay = min(wire0.get(&pos).unwrap() + distance, min_sig_delay);
    }
    println!("Answer to day 3 part 1 is {}", min_manhattan);
    println!("Answer to day 3 part 2 is {}", min_sig_delay);
}

fn incrementor(c: char) -> (isize, isize) {
    let x_inc; 
    let y_inc;
    match c {
        'U' => {
            x_inc = 0;
            y_inc = 1;
        },
        'D' => {
            x_inc = 0;
            y_inc = -1;
        },
        'L' => {
            x_inc = -1;
            y_inc = 0;
        },
        'R' => {
            x_inc = 1;
            y_inc = 0;
        },
        _   => panic!("Bad direction"),
    }
    (x_inc, y_inc)
}

fn init_wire(dir_str: &str) -> HashMap<Position, isize> {
    let directions = dir_str.split(",").map(|s| s.trim());
    let mut x = 0;
    let mut y = 0;
    let mut wire: HashMap<Position, isize> = HashMap::new();
    let mut distance = 0;
    for dir in directions {
        let mut dir_chars = dir.chars();
        let (x_inc, y_inc) = incrementor(dir_chars.next().unwrap()); // parse direction
        let mut section_len = dir_chars.collect::<String>().parse::<isize>().unwrap();

        while section_len > 0 {
            let pos = Position{x,y};
            if !wire.contains_key(&pos) {
                wire.insert(pos, distance);
            }
            x += x_inc;
            y += y_inc;
            section_len -= 1;
            distance += 1;
        }

        let endpos = Position {x,y};
        wire.insert(endpos, distance);
    }
    wire
}