use std::collections::hash_set::*;

#[derive(PartialEq, Eq, Hash, Clone)]
struct Position {
    x: isize,
    y: isize,
}

pub fn solve(input: &str) {
    println!("Doing day 3");
    let wires: Vec<&str> = input.split_whitespace().collect();
    
    let wire0 = init_wire(wires[0]);
    let wire1 = init_wire(wires[1]);
    let intersections: HashSet<Position> = 
        wire0.intersection(&wire1).filter(|pos| pos.x != 0 && pos.y != 0)
        .cloned()
        .collect();

    let shortest = intersections.into_iter()
        .map(|pos| pos.x.abs() + pos.y.abs())
        .min().unwrap();
    
    println!("Answer to day 3 part 1 is {}", shortest);
}

fn init_wire(dir_str: &str) -> HashSet<Position> {
    let directions = dir_str.split(",").map(|s| s.trim());
    let mut x = 0;
    let mut y = 0;
    let mut wire: HashSet<Position> = HashSet::new();
    for dir in directions {
        let mut dir_chars = dir.chars();
        let first_ch = dir_chars.next().unwrap();
        let mut distance = dir_chars.collect::<String>().parse::<isize>().unwrap();

        match first_ch {
            'U' => {
                while distance > 0 {
                    wire.insert(Position{x,y});
                    y += 1;
                    distance -= 1;
                }
            },
            'D' => {
                while distance > 0 {
                    wire.insert(Position{x,y});
                    y -= 1;
                    distance -= 1;
                }
            },
            'L' => {
                while distance > 0 {
                    wire.insert(Position{x,y});
                    x -= 1;
                    distance -= 1;
                }
            },
            'R' => {
                while distance > 0 {
                    wire.insert(Position{x,y});
                    x += 1;
                    distance -= 1;
                }
            },
            _   => panic!("Bad direction"),
        }
        let endpos = Position {x,y};
        wire.insert(endpos);
    }
    wire
}