#!/usr/bin/ruby

total = 0
$stdin.each do |value|
  fuel = value.to_i/3-2
  while (fuel>0)
    total += fuel
    fuel = fuel/3-2
  end
end
puts(total)
