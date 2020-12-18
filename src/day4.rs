pub fn solve() {
    println!("Doing day 4");
    let pw_candidates: Vec<usize> = (136760..595730).filter(|x| valid_password(*x)).collect();
    println!("Answer to Day 4 part 1 is {}", pw_candidates.len());
    
    let final_count = pw_candidates.iter().filter(|x| has_two_adjacent(**x)).count();
    println!("Answer to Day 4 part 2 is {}", final_count);
}

/// Return true if contains repeated digits and no decreasing from left to right
fn valid_password(u: usize) -> bool {
    let mut u = u;
    let mut repeat_digits = false;
    let mut prev = u % 10;
    while u > 0 {
        u /= 10;
        let digit = u % 10;
        if digit > prev {
            return false;
        }
        if digit == prev {
            repeat_digits = true;
        }
        prev = digit;
    }
    repeat_digits
}

fn has_two_adjacent(u: usize) -> bool {
    let mut u = u;
    let mut seen_two = false;
    let mut seen_over_two = false;

    let mut prev = u % 10;
    while u > 0 {
        u /= 10;
        let curr = u % 10;
        if seen_two {
            if curr != prev {
                return true;
            } else {
                seen_over_two = true;
                seen_two = false;
            }
        } else if seen_over_two {
            seen_over_two = curr == prev;
        } else if curr == prev {
            seen_two = true;
        }
        prev = curr;
    }
    seen_two
}

#[test]
fn test_two_adjacent() {
    assert!(has_two_adjacent(12234));
    assert!(!has_two_adjacent(122234));
}