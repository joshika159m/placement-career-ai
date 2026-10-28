"""
Predefined Question Bank for Live Aptitude Assessment
Contains 80 verified questions across 4 categories:
- Quantitative Aptitude (20 questions)
- Logical Reasoning (20 questions)
- Verbal Ability (20 questions)
- Data Interpretation (20 questions)
"""

APTITUDE_QUESTIONS = [
    # ==========================================
    # 1. QUANTITATIVE APTITUDE (IDs 1 - 20)
    # ==========================================
    {
        "id": 1,
        "category": "Quantitative Aptitude",
        "question": "A train 240 m long passes a pole in 24 seconds. How long will it take to pass a platform 650 m long?",
        "options": ["65 seconds", "89 seconds", "100 seconds", "150 seconds"],
        "answer": "89 seconds",
        "explanation": "Speed of train = 240/24 = 10 m/s. Total distance to pass platform = 240 + 650 = 890 m. Time = 890/10 = 89 seconds."
    },
    {
        "id": 2,
        "category": "Quantitative Aptitude",
        "question": "If a person sells an article for Rs. 720, he incurs a loss of 20%. At what price should he sell it to gain 20%?",
        "options": ["Rs. 900", "Rs. 1000", "Rs. 1080", "Rs. 1200"],
        "answer": "Rs. 1080",
        "explanation": "Cost Price = 720 / 0.8 = Rs. 900. Required Selling Price for 20% gain = 900 * 1.2 = Rs. 1080."
    },
    {
        "id": 3,
        "category": "Quantitative Aptitude",
        "question": "A and B can complete a work in 12 days and 18 days respectively. If they work together, in how many days will the work be completed?",
        "options": ["6.5 days", "7.2 days", "8.0 days", "9.4 days"],
        "answer": "7.2 days",
        "explanation": "Combined 1 day work = 1/12 + 1/18 = (3 + 2)/36 = 5/36. Total days = 36/5 = 7.2 days."
    },
    {
        "id": 4,
        "category": "Quantitative Aptitude",
        "question": "The ratio of ages of father and son is 7:3. If the sum of their ages is 60 years, what was the son's age 5 years ago?",
        "options": ["13 years", "18 years", "23 years", "25 years"],
        "answer": "13 years",
        "explanation": "Sum of ratios = 7 + 3 = 10. Son's current age = (3/10) * 60 = 18 years. Age 5 years ago = 18 - 5 = 13 years."
    },
    {
        "id": 5,
        "category": "Quantitative Aptitude",
        "question": "What is the compound interest on Rs. 10,000 for 2 years at 10% per annum, compounded annually?",
        "options": ["Rs. 2000", "Rs. 2100", "Rs. 2200", "Rs. 2500"],
        "answer": "Rs. 2100",
        "explanation": "Amount = 10000 * (1 + 10/100)^2 = 10000 * 1.21 = Rs. 12,100. CI = 12100 - 10000 = Rs. 2100."
    },
    {
        "id": 6,
        "category": "Quantitative Aptitude",
        "question": "Two cards are drawn from a well-shuffled pack of 52 cards without replacement. What is the probability that both are aces?",
        "options": ["1/221", "1/169", "4/663", "2/52"],
        "answer": "1/221",
        "explanation": "Probability = (4/52) * (3/51) = (1/13) * (1/17) = 1/221."
    },
    {
        "id": 7,
        "category": "Quantitative Aptitude",
        "question": "In how many different ways can the letters of the word 'LEADER' be arranged?",
        "options": ["720", "360", "120", "48"],
        "answer": "360",
        "explanation": "Total letters = 6, with 'E' repeating twice. Total permutations = 6! / 2! = 720 / 2 = 360."
    },
    {
        "id": 8,
        "category": "Quantitative Aptitude",
        "question": "The average of 5 consecutive odd numbers is 27. What is the product of the first and the last number?",
        "options": ["621", "667", "713", "765"],
        "answer": "713",
        "explanation": "If average is 27, the 5 consecutive odd numbers are 23, 25, 27, 29, 31. Product of first and last = 23 * 31 = 713."
    },
    {
        "id": 9,
        "category": "Quantitative Aptitude",
        "question": "A car travels at 60 km/h for the first 2 hours and at 90 km/h for the next 3 hours. What is its average speed for the entire journey?",
        "options": ["72 km/h", "75 km/h", "78 km/h", "80 km/h"],
        "answer": "78 km/h",
        "explanation": "Total distance = (60 * 2) + (90 * 3) = 120 + 270 = 390 km. Total time = 5 hours. Average speed = 390 / 5 = 78 km/h."
    },
    {
        "id": 10,
        "category": "Quantitative Aptitude",
        "question": "A pipe can fill a tank in 10 hours, while another pipe empties it in 15 hours. How long will it take to fill the tank if both are opened together?",
        "options": ["25 hours", "30 hours", "35 hours", "20 hours"],
        "answer": "30 hours",
        "explanation": "Net filling per hour = 1/10 - 1/15 = (3 - 2)/30 = 1/30. Time required = 30 hours."
    },
    {
        "id": 11,
        "category": "Quantitative Aptitude",
        "question": "If 20% of a number is equal to two-third of another number, what is the ratio of first number to the second number?",
        "options": ["2:5", "3:10", "10:3", "5:2"],
        "answer": "10:3",
        "explanation": "0.20 * A = (2/3) * B => (1/5) * A = (2/3) * B => A / B = (2/3) * 5 = 10/3 => 10:3."
    },
    {
        "id": 12,
        "category": "Quantitative Aptitude",
        "question": "What is the greatest number that will divide 390, 495, and 300 without leaving a remainder?",
        "options": ["5", "15", "25", "30"],
        "answer": "15",
        "explanation": "GCD of 390, 495, and 300: 390 = 15*26, 495 = 15*33, 300 = 15*20. Hence HCF = 15."
    },
    {
        "id": 13,
        "category": "Quantitative Aptitude",
        "question": "A man buys milk at Rs. 20 per litre and adds water equal to 25% of the milk volume. If he sells the mixture at Rs. 20 per litre, what is his profit percentage?",
        "options": ["20%", "25%", "30%", "33.33%"],
        "answer": "25%",
        "explanation": "Water costs Rs. 0. If 4 litres of milk (cost Rs. 80) is diluted with 1 litre water, he sells 5 litres for Rs. 100. Profit = (20/80)*100 = 25%."
    },
    {
        "id": 14,
        "category": "Quantitative Aptitude",
        "question": "The perimeter of a rectangular field is 160 m and the difference between two adjacent sides is 48 m. Find the length of the larger side.",
        "options": ["32 m", "48 m", "64 m", "80 m"],
        "answer": "64 m",
        "explanation": "2*(L + B) = 160 => L + B = 80. Also L - B = 48. Adding both: 2L = 128 => L = 64 m."
    },
    {
        "id": 15,
        "category": "Quantitative Aptitude",
        "question": "A boat can travel with a speed of 13 km/h in still water. If the speed of the stream is 4 km/h, find the time taken by the boat to go 68 km downstream.",
        "options": ["3 hours", "4 hours", "5 hours", "6 hours"],
        "answer": "4 hours",
        "explanation": "Downstream speed = 13 + 4 = 17 km/h. Time taken = 68 / 17 = 4 hours."
    },
    {
        "id": 16,
        "category": "Quantitative Aptitude",
        "question": "Find the sum of all two-digit numbers divisible by 5.",
        "options": ["945", "950", "990", "1000"],
        "answer": "945",
        "explanation": "Numbers are 10, 15, 20, ..., 95. First term a=10, last term l=95, d=5. Number of terms n = (95-10)/5 + 1 = 18. Sum = 18/2 * (10 + 95) = 9 * 105 = 945."
    },
    {
        "id": 17,
        "category": "Quantitative Aptitude",
        "question": "If 6 men or 8 women can reap a field in 86 days, how long will 14 men and 10 women take to reap it?",
        "options": ["24 days", "28 days", "32 days", "36 days"],
        "answer": "24 days",
        "explanation": "6 Men = 8 Women => 1 Man = 4/3 Women. 14 Men + 10 Women = 14*(4/3) + 10 = 56/3 + 30/3 = 86/3 Women. 8 Women take 86 days. Days = (8 * 86) / (86/3) = 24 days."
    },
    {
        "id": 18,
        "category": "Quantitative Aptitude",
        "question": "A sum of money doubles itself in 8 years at simple interest. In how many years will it triple itself?",
        "options": ["12 years", "14 years", "16 years", "20 years"],
        "answer": "16 years",
        "explanation": "Simple Interest = P in 8 years, meaning interest rate = 100/8 = 12.5%. To triple, interest needed = 2P. Time = 2P / (P * 0.125) = 16 years."
    },
    {
        "id": 19,
        "category": "Quantitative Aptitude",
        "question": "The diagonal of a square is 10 cm. What is its area?",
        "options": ["25 sq cm", "50 sq cm", "75 sq cm", "100 sq cm"],
        "answer": "50 sq cm",
        "explanation": "Area of square = (diagonal^2) / 2 = (10^2) / 2 = 100 / 2 = 50 sq cm."
    },
    {
        "id": 20,
        "category": "Quantitative Aptitude",
        "question": "In an examination, 35% of total students failed in Hindi, 45% in English, and 20% in both. What percentage of students passed in both subjects?",
        "options": ["35%", "40%", "45%", "50%"],
        "answer": "40%",
        "explanation": "Failed in at least one = 35 + 45 - 20 = 60%. Percentage passed in both = 100 - 60 = 40%."
    },

    # ==========================================
    # 2. LOGICAL REASONING (IDs 21 - 40)
    # ==========================================
    {
        "id": 21,
        "category": "Logical Reasoning",
        "question": "Look at this series: 2, 1, (1/2), (1/4), ... What number should come next?",
        "options": ["(1/3)", "(1/8)", "(2/8)", "(1/16)"],
        "answer": "(1/8)",
        "explanation": "This is a simple division series; each number is half of the previous number: (1/4)/2 = 1/8."
    },
    {
        "id": 22,
        "category": "Logical Reasoning",
        "question": "Pointing to a photograph, a man said, 'I have no brother or sister, but that man's father is my father's son.' Whose photograph was it?",
        "options": ["His own", "His son's", "His father's", "His nephew's"],
        "answer": "His son's",
        "explanation": "Since the speaker has no brother or sister, 'my father's son' is himself. So 'that man's father is myself', which means the photograph is of his son."
    },
    {
        "id": 23,
        "category": "Logical Reasoning",
        "question": "If in a code language, 'ROSE' is written as 'ILHV', how is 'HAND' written in that code?",
        "options": ["SZMW", "TBNF", "SZMV", "RYLW"],
        "answer": "SZMW",
        "explanation": "Each letter is paired with its reverse alphabet counterpart (A-Z, B-Y, etc.): H <-> S, A <-> Z, N <-> M, D <-> W. So 'SZMW'."
    },
    {
        "id": 24,
        "category": "Logical Reasoning",
        "question": "Statements: (1) All dogs are cats. (2) All cats are birds. Conclusions: I. All dogs are birds. II. All birds are dogs.",
        "options": ["Only conclusion I follows", "Only conclusion II follows", "Both I and II follow", "Neither I nor II follows"],
        "answer": "Only conclusion I follows",
        "explanation": "All dogs are cats and all cats are birds implies Dogs are a subset of Birds. Therefore, All dogs are birds follows, but the reverse does not."
    },
    {
        "id": 25,
        "category": "Logical Reasoning",
        "question": "A person walks 5 km North, turns right and walks 3 km, turns right and walks 5 km. How far and in what direction is he from his starting point?",
        "options": ["3 km East", "3 km West", "5 km North", "8 km South"],
        "answer": "3 km East",
        "explanation": "Walking 5 km North and then 5 km South cancels the North-South movement. The person is 3 km East of the origin."
    },
    {
        "id": 26,
        "category": "Logical Reasoning",
        "question": "Find the odd one out: 27, 64, 125, 144, 216, 343.",
        "options": ["64", "125", "144", "343"],
        "answer": "144",
        "explanation": "All other numbers are perfect cubes: 27=3^3, 64=4^3, 125=5^3, 216=6^3, 343=7^3. 144 is 12^2 (not a cube of an integer)."
    },
    {
        "id": 27,
        "category": "Logical Reasoning",
        "question": "If Monday falls on 1st of a month, which day of the week will fall on the 25th of the same month?",
        "options": ["Wednesday", "Thursday", "Friday", "Saturday"],
        "answer": "Thursday",
        "explanation": "Day difference = 25 - 1 = 24 days. 24 mod 7 = 3 odd days. Monday + 3 days = Thursday."
    },
    {
        "id": 28,
        "category": "Logical Reasoning",
        "question": "Five friends P, Q, R, S, T are sitting in a row facing North. S is between T and Q. Q is to the immediate left of R. P is to the immediate left of T. Who is in the middle?",
        "options": ["P", "T", "S", "Q"],
        "answer": "S",
        "explanation": "Order from left to right: P, T, S, Q, R. S is exactly in the middle position."
    },
    {
        "id": 29,
        "category": "Logical Reasoning",
        "question": "At what angle are the hands of a clock inclined at 15 minutes past 5?",
        "options": ["58.5 degrees", "64 degrees", "67.5 degrees", "72.5 degrees"],
        "answer": "67.5 degrees",
        "explanation": "Minute hand angle = 15 * 6 = 90 deg. Hour hand angle = 5 * 30 + 15 * 0.5 = 150 + 7.5 = 157.5 deg. Angle difference = 157.5 - 90 = 67.5 degrees."
    },
    {
        "id": 30,
        "category": "Logical Reasoning",
        "question": "Cup is to Coffee as Bowl is to: ",
        "options": ["Dish", "Soup", "Spoon", "Food"],
        "answer": "Soup",
        "explanation": "A cup is used to hold coffee; similarly, a bowl is primarily used to hold soup."
    },
    {
        "id": 31,
        "category": "Logical Reasoning",
        "question": "In a certain code, '253' means 'books are old', '546' means 'man is old', and '378' means 'buy good books'. What is the code for 'are'?",
        "options": ["2", "3", "5", "6"],
        "answer": "2",
        "explanation": "From 1st and 2nd, '5' = 'old'. From 1st and 3rd, '3' = 'books'. Therefore in 1st statement, '2' = 'are'."
    },
    {
        "id": 32,
        "category": "Logical Reasoning",
        "question": "Statements: Most doctors are hard-working. Raman is a doctor. Conclusions: I. Raman is hard-working. II. Raman may be hard-working.",
        "options": ["Only conclusion I follows", "Only conclusion II follows", "Either I or II follows", "Neither follows"],
        "answer": "Only conclusion II follows",
        "explanation": "Since 'most' means not all, it is possible but not definite that Raman is hard-working. Hence only conclusion II (possibility) follows."
    },
    {
        "id": 33,
        "category": "Logical Reasoning",
        "question": "Complete the series: B2D, D4F, F6H, H8J, ...?",
        "options": ["J10L", "J10K", "I10L", "K10M"],
        "answer": "J10L",
        "explanation": "First letter: B(+2)=D(+2)=F(+2)=H(+2)=J. Number: 2(+2)=4(+2)=6(+2)=8(+2)=10. Last letter: D(+2)=F(+2)=H(+2)=J(+2)=L. Next is J10L."
    },
    {
        "id": 34,
        "category": "Logical Reasoning",
        "question": "If '+' means multiply, '-' means divide, '*' means add, and '/' means subtract, evaluate: 20 - 4 + 6 * 8 / 4.",
        "options": ["34", "30", "28", "24"],
        "answer": "34",
        "explanation": "Rewriting with operators: 20 / 4 * 6 + 8 - 4 = 5 * 6 + 8 - 4 = 30 + 8 - 4 = 34."
    },
    {
        "id": 35,
        "category": "Logical Reasoning",
        "question": "A is B's sister. C is B's mother. D is C's father. E is D's mother. How is A related to D?",
        "options": ["Grandmother", "Granddaughter", "Daughter", "Grandfather"],
        "answer": "Granddaughter",
        "explanation": "A is daughter of C, and D is father of C. Thus, A is the granddaughter of D."
    },
    {
        "id": 36,
        "category": "Logical Reasoning",
        "question": "Which word does NOT belong with the others?",
        "options": ["Parsley", "Basil", "Dill", "Mayonnaise"],
        "answer": "Mayonnaise",
        "explanation": "Parsley, basil, and dill are herbs; mayonnaise is a condiment/sauce."
    },
    {
        "id": 37,
        "category": "Logical Reasoning",
        "question": "If South-East becomes North, North-East becomes West and so on, what will West become?",
        "options": ["South-East", "North-East", "South-West", "North-West"],
        "answer": "South-East",
        "explanation": "Every direction turns 135 degrees anti-clockwise. Turning West 135 degrees anti-clockwise gives South-East."
    },
    {
        "id": 38,
        "category": "Logical Reasoning",
        "question": "In a row of 40 students, Amit is 18th from the left. What is his rank from the right end?",
        "options": ["22nd", "23rd", "24th", "21st"],
        "answer": "23rd",
        "explanation": "Rank from right = (Total students - Rank from left) + 1 = (40 - 18) + 1 = 22 + 1 = 23rd."
    },
    {
        "id": 39,
        "category": "Logical Reasoning",
        "question": "Find the next term in the alphanumeric series: Z1A, X2D, V6G, T24J, ...?",
        "options": ["R120M", "R96M", "S120L", "Q120M"],
        "answer": "R120M",
        "explanation": "First letter decreases by 2: Z, X, V, T, R. Numbers: 1 (*2) = 2 (*3) = 6 (*4) = 24 (*5) = 120. Last letter increases by 3: A, D, G, J, M. Result: R120M."
    },
    {
        "id": 40,
        "category": "Logical Reasoning",
        "question": "Statement: 'Please do not lean out of the train window.' — Notice on a compartment. Assumption I: Leaning out is dangerous. Assumption II: Passengers can read notices.",
        "options": ["Only assumption I is implicit", "Only assumption II is implicit", "Both I and II are implicit", "Neither is implicit"],
        "answer": "Both I and II are implicit",
        "explanation": "Warnings are issued because the act is dangerous (Assumption I) and printed notices presume readers can understand them (Assumption II)."
    },

    # ==========================================
    # 3. VERBAL ABILITY (IDs 41 - 60)
    # ==========================================
    {
        "id": 41,
        "category": "Verbal Ability",
        "question": "Choose the word most nearly OPPOSITE in meaning to 'METICULOUS':",
        "options": ["Careless", "Thorough", "Detailed", "Painstaking"],
        "answer": "Careless",
        "explanation": "'Meticulous' means showing great attention to detail. The opposite is 'Careless'."
    },
    {
        "id": 42,
        "category": "Verbal Ability",
        "question": "Select the correct SYNONYM of the word 'PRAGMATIC':",
        "options": ["Idealistic", "Theoretical", "Practical", "Romantic"],
        "answer": "Practical",
        "explanation": "'Pragmatic' means dealing with things sensibly and realistically in a practical way."
    },
    {
        "id": 43,
        "category": "Verbal Ability",
        "question": "Identify the error in the sentence: 'Neither the manager nor the employees (A) / was present (B) / at the annual meeting (C) / yesterday (D).'",
        "options": ["Part A", "Part B", "Part C", "Part D"],
        "answer": "Part B",
        "explanation": "When two subjects are joined by 'neither... nor', the verb agrees with the closer subject ('employees' is plural, so it should be 'were present')."
    },
    {
        "id": 44,
        "category": "Verbal Ability",
        "question": "Fill in the blank: The committee decided to _____ the proposal until further market data became available.",
        "options": ["defer", "differ", "defy", "deter"],
        "answer": "defer",
        "explanation": "'Defer' means to put off or postpone to a later time."
    },
    {
        "id": 45,
        "category": "Verbal Ability",
        "question": "Choose the one-word substitution for: 'A person who speaks many languages.'",
        "options": ["Linguist", "Polyglot", "Grammarian", "Bilingual"],
        "answer": "Polyglot",
        "explanation": "A 'Polyglot' is someone who knows and is able to use several languages."
    },
    {
        "id": 46,
        "category": "Verbal Ability",
        "question": "Choose the correct idiom meaning for: 'To burn the candle at both ends'",
        "options": ["To waste candle wax", "To work extremely hard from early morning to late night", "To be careless with money", "To cause conflicts"],
        "answer": "To work extremely hard from early morning to late night",
        "explanation": "Burning the candle at both ends means overworking oneself and exhausting one's physical energy."
    },
    {
        "id": 47,
        "category": "Verbal Ability",
        "question": "Fill in the blank with appropriate preposition: She has been suffering _____ severe migraines since childhood.",
        "options": ["with", "of", "from", "by"],
        "answer": "from",
        "explanation": "The standard grammatical colocation for illnesses is 'suffering from'."
    },
    {
        "id": 48,
        "category": "Verbal Ability",
        "question": "Select the correctly spelt word:",
        "options": ["Accomodate", "Accommodate", "Acomodate", "Acommodate"],
        "answer": "Accommodate",
        "explanation": "The correct spelling is 'Accommodate' with double 'c' and double 'm'."
    },
    {
        "id": 49,
        "category": "Verbal Ability",
        "question": "Identify the sentence with correct punctuation and grammar:",
        "options": [
            "Its a well known fact that honesty is best policy.",
            "It's a well-known fact that honesty is the best policy.",
            "Its a well-known fact that honesty is the best policy.",
            "It's a well known fact that honesty is best policy."
        ],
        "answer": "It's a well-known fact that honesty is the best policy.",
        "explanation": "'It's' is the contraction of 'it is', 'well-known' is a hyphenated compound adjective, and 'the best policy' includes the required article."
    },
    {
        "id": 50,
        "category": "Verbal Ability",
        "question": "Choose the correct passive form of: 'The chef prepared a lavish dinner for the guests.'",
        "options": [
            "A lavish dinner was prepared by the chef for the guests.",
            "A lavish dinner had been prepared by the chef for the guests.",
            "A lavish dinner is prepared by the chef for the guests.",
            "A lavish dinner was being prepared by the chef for the guests."
        ],
        "answer": "A lavish dinner was prepared by the chef for the guests.",
        "explanation": "Simple past active ('prepared') changes to simple past passive ('was prepared')."
    },
    {
        "id": 51,
        "category": "Verbal Ability",
        "question": "Choose the word most nearly OPPOSITE to 'LUCID':",
        "options": ["Clear", "Obscure", "Transparent", "Bright"],
        "answer": "Obscure",
        "explanation": "'Lucid' means expressed clearly or easy to understand. The opposite is 'Obscure'."
    },
    {
        "id": 52,
        "category": "Verbal Ability",
        "question": "Rearrange the jumbled parts into a coherent sentence: (P) in spite of (Q) he succeeded (R) difficulties (S) all the",
        "options": ["Q P S R", "P S R Q", "R S P Q", "S R P Q"],
        "answer": "Q P S R",
        "explanation": "Sentence: 'He succeeded (Q) in spite of (P) all the (S) difficulties (R).' Matches Q-P-S-R."
    },
    {
        "id": 53,
        "category": "Verbal Ability",
        "question": "Fill in the blank: Despite her initial reluctance, she finally agreed to _____ to their demands.",
        "options": ["accede", "exceed", "concede", "recede"],
        "answer": "accede",
        "explanation": "'Accede' means to agree to a demand, request, or treaty."
    },
    {
        "id": 54,
        "category": "Verbal Ability",
        "question": "Choose the idiom meaning of: 'Bite the bullet'",
        "options": ["To eat quickly", "To face a difficult or unpleasant situation with courage", "To initiate a dispute", "To run away from danger"],
        "answer": "To face a difficult or unpleasant situation with courage",
        "explanation": "Biting the bullet means enduring an inevitable painful situation bravely."
    },
    {
        "id": 55,
        "category": "Verbal Ability",
        "question": "Find the synonym of 'CANDID':",
        "options": ["Frank", "Deceitful", "Shy", "Reserved"],
        "answer": "Frank",
        "explanation": "'Candid' means truthful and straightforward; frank."
    },
    {
        "id": 56,
        "category": "Verbal Ability",
        "question": "Spot the error: 'He is one of those writers (A) / who has won (B) / international acclaim (C) / this decade (D).'",
        "options": ["Part A", "Part B", "Part C", "Part D"],
        "answer": "Part B",
        "explanation": "The antecedent of relative pronoun 'who' is plural 'writers', so the plural verb 'have won' must be used instead of 'has won'."
    },
    {
        "id": 57,
        "category": "Verbal Ability",
        "question": "Choose the word that means 'A state of temporary disuse or suspension':",
        "options": ["Abeyance", "Abscond", "Abstinence", "Aberration"],
        "answer": "Abeyance",
        "explanation": "'Abeyance' refers to a state of temporary disuse, inactivity, or suspension."
    },
    {
        "id": 58,
        "category": "Verbal Ability",
        "question": "Fill in the blank: The technology startup demonstrated an _____ ability to adapt to changing market requirements.",
        "options": ["uncanny", "uncouth", "unctuous", "unruly"],
        "answer": "uncanny",
        "explanation": "'Uncanny' means strange or mysterious, often used in positive context like 'uncanny ability' (extraordinary knack)."
    },
    {
        "id": 59,
        "category": "Verbal Ability",
        "question": "Choose the correct indirect speech: He said, 'I have completed my software project.'",
        "options": [
            "He said that he had completed his software project.",
            "He said that he has completed his software project.",
            "He said that he completed his software project.",
            "He told that he had completed his software project."
        ],
        "answer": "He said that he had completed his software project.",
        "explanation": "Present perfect ('have completed') shifts to past perfect ('had completed') in indirect speech."
    },
    {
        "id": 60,
        "category": "Verbal Ability",
        "question": "Choose the antonym of 'EPHEMERAL':",
        "options": ["Transitory", "Eternal", "Brief", "Fleeting"],
        "answer": "Eternal",
        "explanation": "'Ephemeral' means lasting for a very short time. The opposite is 'Eternal' or permanent."
    },

    # ==========================================
    # 4. DATA INTERPRETATION (IDs 61 - 80)
    # ==========================================
    {
        "id": 61,
        "category": "Data Interpretation",
        "question": "A table shows revenue of a company: 2021 = $40M, 2022 = $50M, 2023 = $65M. What is the percentage increase in revenue from 2021 to 2023?",
        "options": ["50.0%", "62.5%", "75.0%", "80.0%"],
        "answer": "62.5%",
        "explanation": "Increase = 65 - 40 = $25M. Percentage increase = (25 / 40) * 100 = 62.5%."
    },
    {
        "id": 62,
        "category": "Data Interpretation",
        "question": "In a pie chart representing monthly college expenses, Tuition accounts for 108 degrees of the central angle. What percentage of total expenditure is Tuition?",
        "options": ["25%", "30%", "33.33%", "36%"],
        "answer": "30%",
        "explanation": "Total central angle = 360 degrees. Percentage = (108 / 360) * 100 = 30%."
    },
    {
        "id": 63,
        "category": "Data Interpretation",
        "question": "A company has 4 departments with employee counts: Engineering (120), Marketing (60), HR (30), Sales (90). What is the ratio of Engineering employees to total employees?",
        "options": ["1:2", "2:5", "3:7", "4:9"],
        "answer": "2:5",
        "explanation": "Total employees = 120 + 60 + 30 + 90 = 300. Ratio = 120 / 300 = 2 / 5 (2:5)."
    },
    {
        "id": 64,
        "category": "Data Interpretation",
        "question": "The average monthly salaries in thousands for 5 engineers are 45, 55, 60, 70, 90. What is the median salary?",
        "options": ["55 thousand", "60 thousand", "64 thousand", "70 thousand"],
        "answer": "60 thousand",
        "explanation": "Arranged in ascending order: 45, 55, 60, 70, 90. The middle element (3rd) is 60 thousand."
    },
    {
        "id": 65,
        "category": "Data Interpretation",
        "question": "A factory produces 400 widgets on Monday, 450 on Tuesday, 500 on Wednesday, 480 on Thursday, and 520 on Friday. What is the average daily production?",
        "options": ["460", "470", "480", "490"],
        "answer": "470",
        "explanation": "Total production = 400 + 450 + 500 + 480 + 520 = 2350 widgets. Average = 2350 / 5 = 470."
    },
    {
        "id": 66,
        "category": "Data Interpretation",
        "question": "In a class of 80 students, 60% are boys. If 25% of boys and 50% of girls play football, how many total students play football?",
        "options": ["24", "28", "32", "36"],
        "answer": "28",
        "explanation": "Boys = 80 * 0.6 = 48. Girls = 80 - 48 = 32. Football playing boys = 48 * 0.25 = 12. Football playing girls = 32 * 0.50 = 16. Total = 12 + 16 = 28."
    },
    {
        "id": 67,
        "category": "Data Interpretation",
        "question": "A bar chart shows car sales over 4 quarters: Q1=150, Q2=200, Q3=250, Q4=180. Which quarter showed the highest quarter-over-quarter percentage growth?",
        "options": ["Q2", "Q3", "Q4", "Both Q2 and Q3"],
        "answer": "Q2",
        "explanation": "Q1 to Q2 growth = (200-150)/150 = 50/150 = 33.33%. Q2 to Q3 growth = (250-200)/200 = 50/200 = 25.0%. Q3 to Q4 decreased. Highest is Q2 (33.33%)."
    },
    {
        "id": 68,
        "category": "Data Interpretation",
        "question": "In a survey of 500 tech employees: 280 know Python, 220 know Java, and 100 know both. How many know neither Python nor Java?",
        "options": ["80", "100", "120", "150"],
        "answer": "100",
        "explanation": "Employees knowing at least one language = 280 + 220 - 100 = 400. Knowing neither = 500 - 400 = 100."
    },
    {
        "id": 69,
        "category": "Data Interpretation",
        "question": "A line graph depicts company profits (in lakhs): 2020: 12, 2021: 18, 2022: 15, 2023: 24. What is the average annual profit?",
        "options": ["15.5 lakhs", "17.25 lakhs", "18.0 lakhs", "19.5 lakhs"],
        "answer": "17.25 lakhs",
        "explanation": "Sum of profits = 12 + 18 + 15 + 24 = 69 lakhs. Average = 69 / 4 = 17.25 lakhs."
    },
    {
        "id": 70,
        "category": "Data Interpretation",
        "question": "In a college placement drive, 120 students applied for Software Engineering, 80 for Data Science, and 50 for Cyber Security. What percentage of total applicants chose Data Science?",
        "options": ["28%", "32%", "35%", "40%"],
        "answer": "32%",
        "explanation": "Total applicants = 120 + 80 + 50 = 250. Percentage for Data Science = (80 / 250) * 100 = 32%."
    },
    {
        "id": 71,
        "category": "Data Interpretation",
        "question": "Table of marks scored by a student: Math=85/100, Physics=75/100, Chemistry=80/100, English=90/100, CS=95/100. What is his overall aggregate percentage?",
        "options": ["82%", "85%", "86%", "88%"],
        "answer": "85%",
        "explanation": "Total marks scored = 85 + 75 + 80 + 90 + 95 = 425 out of 500. Aggregate percentage = (425 / 500) * 100 = 85%."
    },
    {
        "id": 72,
        "category": "Data Interpretation",
        "question": "A pie chart allocates budget across 4 teams: Team A = 40%, Team B = 25%, Team C = 20%, Team D = 15%. If the total budget is $2,000,000, how much more does Team A receive than Team C?",
        "options": ["$300,000", "$400,000", "$500,000", "$600,000"],
        "answer": "$400,000",
        "explanation": "Difference percentage = 40% - 20% = 20%. Difference amount = 0.20 * $2,000,000 = $400,000."
    },
    {
        "id": 73,
        "category": "Data Interpretation",
        "question": "In 2022, a store had sales of 500 units at $20 each. In 2023, sales grew to 600 units at $25 each. What was the percentage increase in total revenue?",
        "options": ["30%", "40%", "50%", "60%"],
        "answer": "50%",
        "explanation": "Revenue 2022 = 500 * 20 = $10,000. Revenue 2023 = 600 * 25 = $15,000. Increase = (15000 - 10000)/10000 = 50%."
    },
    {
        "id": 74,
        "category": "Data Interpretation",
        "question": "Exam pass percentages across 3 sections: Sec A has 40 students with 80% pass rate; Sec B has 50 students with 70% pass rate; Sec C has 60 students with 90% pass rate. How many total students passed?",
        "options": ["115", "121", "125", "130"],
        "answer": "121",
        "explanation": "Passed in A = 40 * 0.8 = 32. Passed in B = 50 * 0.7 = 35. Passed in C = 60 * 0.9 = 54. Total passed = 32 + 35 + 54 = 121."
    },
    {
        "id": 75,
        "category": "Data Interpretation",
        "question": "A company's expenditure on Raw Material is 45% and on Labor is 30%. If Labor costs $150,000, what is the cost of Raw Material?",
        "options": ["$200,000", "$225,000", "$250,000", "$300,000"],
        "answer": "$225,000",
        "explanation": "Total budget = 150,000 / 0.30 = $500,000. Raw material cost = 500,000 * 0.45 = $225,000."
    },
    {
        "id": 76,
        "category": "Data Interpretation",
        "question": "A production line has an error rate of 2% in Batch 1 (10,000 items) and 4% in Batch 2 (5,000 items). What is the overall percentage of defective items across both batches?",
        "options": ["2.50%", "2.67%", "3.00%", "3.33%"],
        "answer": "2.67%",
        "explanation": "Defects in Batch 1 = 200. Defects in Batch 2 = 200. Total defects = 400 out of 15,000 items. Percentage = (400 / 15000) * 100 = 2.67%."
    },
    {
        "id": 77,
        "category": "Data Interpretation",
        "question": "Over 3 years, a student's coding contest scores were: Year 1 = 1200, Year 2 = 1500, Year 3 = 1800. What is the compound annual growth rate (or overall percent growth from Year 1 to 3)?",
        "options": ["33.33%", "40.00%", "50.00%", "60.00%"],
        "answer": "50.00%",
        "explanation": "Overall percentage growth = (1800 - 1200) / 1200 * 100 = 600 / 1200 * 100 = 50.0%."
    },
    {
        "id": 78,
        "category": "Data Interpretation",
        "question": "In a test with 60 questions, a student scored 45 correct, 10 incorrect, and left 5 unattempted. If each correct answer awards 2 marks and each incorrect penalizes 0.5 marks, find net score.",
        "options": ["80 marks", "85 marks", "87.5 marks", "90 marks"],
        "answer": "85 marks",
        "explanation": "Gross marks = 45 * 2 = 90. Penalty = 10 * 0.5 = 5. Net score = 90 - 5 = 85 marks."
    },
    {
        "id": 79,
        "category": "Data Interpretation",
        "question": "A table compares bug resolution times across 3 teams: Team Alpha (4 hours/bug, resolved 30 bugs), Team Beta (6 hours/bug, resolved 20 bugs). What is the combined average time spent per bug?",
        "options": ["4.5 hours", "4.8 hours", "5.0 hours", "5.2 hours"],
        "answer": "4.8 hours",
        "explanation": "Total hours = (30 * 4) + (20 * 6) = 120 + 120 = 240 hours. Total bugs = 50. Average time = 240 / 50 = 4.8 hours/bug."
    },
    {
        "id": 80,
        "category": "Data Interpretation",
        "question": "A radar chart evaluates 4 core skill areas out of 100: Problem Solving=80, Data Structures=85, System Design=70, Communication=75. What is the average skill score?",
        "options": ["76.5", "77.5", "78.0", "79.5"],
        "answer": "77.5",
        "explanation": "Sum of scores = 80 + 85 + 70 + 75 = 310. Average = 310 / 4 = 77.5."
    }
]
