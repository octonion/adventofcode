#!/usr/bin/ruby

total = 0
$stdin.each do |value|
  total += value.to_i/3-2
end
puts(total)
