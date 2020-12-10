use std::fs;
use glob::glob;

mod day1;
mod day2;

fn main() {
    for glob_result in glob("inputs/day?.txt").expect("Failed to read file in inputs") {
        let filepath = glob_result.unwrap();
        let file_stem = filepath.file_stem()
                                .unwrap()
                                .to_str()
                                .unwrap();
        let input = fs::read_to_string(&filepath).unwrap();
        match file_stem {
            "day1" => {
                day1::solve(&input);
            }
            "day2" => {
                day2::solve(&input);
            }
            _ => println!("Given bad file stem name {}", file_stem),
        }
    }
}
