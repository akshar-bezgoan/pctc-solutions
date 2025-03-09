def count_sevens_up_to(num):
    count = 0
    place = 1  
    
    while place <= num:
        higher = num // (place * 10)
        current_digit = (num // place) % 10
        lower = num % place

        if current_digit < 7:
            count += higher * place
        elif current_digit == 7:
            count += higher * place + lower + 1
        else:
            count += (higher + 1) * place

        place *= 10
    
    return count

num = int(input())

sevens = count_sevens_up_to(num)

print(sevens)
