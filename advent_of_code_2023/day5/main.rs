use std::{
    fs::File,
    io::{prelude::*, BufReader},
};

#[derive(Debug)]
struct Instruction {
    index: i64,
    range: i64,
    shift: i64,
}

fn main() -> Result<(), Box<dyn std::error::Error>>{
    let file = File::open("data.txt")?;
    let buf = BufReader::new(file);
    let data: Vec<String> = buf.lines()
        .map(|l| l.expect(""))
        .collect();

    let seeds: Vec<i64> = data[0].split_whitespace().skip(1).map(|num| num.parse().unwrap()).collect();
    println!("seeds: {:?}", seeds);
    let seed_ranges: Vec<(i64, i64)> = seeds.chunks(2).map(|chunk| (chunk[0], chunk[1])).collect();
    println!("seed_ranges: {:?}", seed_ranges);

    let data: Vec<_> = data.iter().skip(3).collect();
    let mut maps: Vec<Vec<Instruction>> = Vec::new();
    let mut buf_vec: Vec<Instruction> = Vec::new();
    for line in data {
        match line.split_whitespace().collect::<Vec<&str>>().as_slice() {
            [num1, num2, num3] => {
                let index: i64 = num1.parse().unwrap();
                let target_index: i64 = num2.parse().unwrap();
                let range: i64 = num3.parse().unwrap();
                
                buf_vec.push(Instruction { index: index, range: range - 1, shift: target_index - index });
            }
            [_, _] => {
                buf_vec.sort_by(|a, b| a.index.cmp(&b.index));
                maps.push(buf_vec);
                buf_vec = Vec::new();
            }
            _ => {}
        }
    };
    buf_vec.sort_by(|a, b| a.index.cmp(&b.index));
    maps.push(buf_vec);
    maps.reverse();
    println!("maps: {:?}", maps[0]);

    let mut s = 0;
    'outer: loop {
        let mut seed = s;
        print!("{}<--", seed);
        for map in &maps {
            for instruction in map {
                if seed < instruction.index {
                    break;
                // } else if instruction.index <= seed && seed <= instruction.index + instruction.range - 1 { // Moved substraction to data parsing
                } else if instruction.index <= seed && seed <= instruction.index + instruction.range {
                    seed += instruction.shift;
                    break;
                }
            }
        }
        println!("{}", seed);
        for (index, length) in &seed_ranges {
            if *index <= seed && seed < index + length {
                println!("{}", s);
                break 'outer      
            }   
        }
        s += 1;
    }

    Ok(())
}