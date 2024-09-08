def merge(array_1, array_2) 
  new_array = [] 
  array_1_pointer = 0 
  array_2_pointer = 0
  # Run the loop until we've reached end of both arrays:
  while array_1_pointer < array_1.length || array_2_pointer < array_2.length
  # If we already reached the end of the first array, # add item from second array:
    if !array_1[array_1_pointer]
      new_array << array_2[array_2_pointer]
      array_2_pointer += 1
  # If we already reached the end of the second array, # add item from first array:
    elsif !array_2[array_2_pointer]
      new_array << array_1[array_1_pointer]
      array_1_pointer += 1
  # If the current number in first array is less than current # number in second array, add from first array:
    elsif array_1[array_1_pointer] < array_2[array_2_pointer]
        new_array << array_1[array_1_pointer]
        array_1_pointer += 1
  # If the current number in second array is less than or equal # to current number in first array, add from second array: 
    else
        new_array << array_2[array_2_pointer]
        array_2_pointer += 1
    end 
  end

  return new_array 
end

array = [1, 2]
puts "This is #{array[0]}" # => nil
