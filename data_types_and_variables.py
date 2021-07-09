# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
(3 + 5 + 1) * 3
# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
(350 * 10) + (400 * 6) + (380 * 4)
# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
enroll_in_class == class_is_not_full and schedule_do_not_conflict
# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
product_offer == purchase_two_items and not_expired
member_product_offer == purchase_two_items or not_expired
# the password must be at least 5 characters
atleast_five_characters = len(password) >= 5
# the username must be no more than 20 characters
less_than_twenty_characters = len(username) <= 20
# the password must not be the same as the username
username_password_not_the_same = password != username
# bonus neither the username or password can start or end with whitespace
