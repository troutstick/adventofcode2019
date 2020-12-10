pub fn solve(input: &str) {
    println!("Doing day 1");
    part1(input);
    part2(input);
}

fn part1(input: &str) {
    let input_iter = input.split_whitespace();
    let ans = input_iter
        .map(|s| s.parse::<i64>().unwrap())
        .map(|i| i / 3 - 2)
        .fold(0, |a,b| a+b);
    println!("The answer to day 1 part 1 is {}", ans);
}

fn part2(input: &str) {
    let input_iter = input.split_whitespace();

    fn calc_fuel(i: i64) -> i64 {
        let fuel_req = i / 3 - 2;
        if fuel_req < 0 { return 0; }
        return fuel_req + calc_fuel(fuel_req);
    };

    let ans = input_iter
        .map(|s| s.parse::<i64>().unwrap())
        .map(calc_fuel)
        .fold(0, |a,b| a+b);
    println!("The answer to day 1 part 2 is {}", ans);
}