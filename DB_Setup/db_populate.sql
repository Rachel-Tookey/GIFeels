USE Mood_Tracker;


INSERT INTO Users
(First_Name, Family_Name, User_Name, Email, Password)
VALUES
('John', 'Doe', 'JoDoe', 'johndoes@example.com', "$2b$12$.VxfEmaBgIMwLNuhfZxmVOXjfo2Xm8K5i1bADqYJmCSu/aTst6IAW"),
('Lucy', 'Smith', 'LSmith', 'lsmith@example.com', "$2b$12$6Y6aUmThOUKmf0DHxEv26OiL/5YfAPMzCLzjKoZ6lHhBW5u3hn0ym");


INSERT INTO Entries
(User_ID, Entry_Date, Emotion, Giph_URL, Choice_J_or_Q, Response_J_or_Q, Diary_Entry)
VALUES 
('1', 20240531, 'frustrated', 'https://media4.giphy.com/media/xUNd9AWlNxNgnxiIxO/200w.mp4?cid=0303f60aw8n6rbf1tb5l49kgndy9ynu24ksk32rvhu477sdi&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'What did the pirate say on his 80th birthday? Aye Matey!', 'Super frustrated!'),
('1', 20240530, 'sad', 'https://media3.giphy.com/media/RIXdN6jjGtRd7dtIMC/200w.mp4?cid=0303f60aivbtq55ms46g8x2r7g2khant5gznuzmqzvkcmdh6&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'They say a person needs just three things to be truly happy in this world: someone to love, something to do, and something to hope for.', 'Today I feel sad!'),
('1', 20240529 'worried', 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTNwdDNhaW8xanRnM2JzcWVxb2V5M25jZnN1dGRjam5zZnc0bmF4aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUPJPzcdlbvaFUrF7y/giphy.mp4', ' Quote', 'If more of us valued food and cheer and song above hoarded gold, it would be a merrier world.', 'I am worried!'),
('1', 20240528, 'worried', 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTNwdDNhaW8xanRnM2JzcWVxb2V5M25jZnN1dGRjam5zZnc0bmF4aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUPJPzcdlbvaFUrF7y/giphy.mp4', 'Joke', 'A man walks into a bar and orders helicopter flavor chips. The barman replies “sorry mate we only do plain”', 'I am worried!'),
('1', 20240527, 'happy', 'https://media0.giphy.com/media/9tzXBdylmxKve/200w.mp4?cid=0303f60alvi8xdy3zog6n5giftaphhaji8f23jdf6z3i9ubr&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'Take responsibility of your own happiness, never put it in other people’s hands.', 'Today I feel happy!'),
('1', 20240526, 'frustrated', 'https://media4.giphy.com/media/xUNd9AWlNxNgnxiIxO/200w.mp4?cid=0303f60aw8n6rbf1tb5l49kgndy9ynu24ksk32rvhu477sdi&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'Happiness is having a large, loving, caring, close-knit family in another city.', 'Super frustrated!'),
('1', 20240525, 'happy', 'https://media0.giphy.com/media/9tzXBdylmxKve/200w.mp4?cid=0303f60alvi8xdy3zog6n5giftaphhaji8f23jdf6z3i9ubr&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'How did Darth Vader know what Luke was getting for Christmas? He felt his presents.', 'Today I feel happy!'),
('1', 20240524, 'happy', 'https://media0.giphy.com/media/9tzXBdylmxKve/200w.mp4?cid=0303f60alvi8xdy3zog6n5giftaphhaji8f23jdf6z3i9ubr&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'In my career as a lumberjack I cut down exactly 52,487 trees. I know because I kept a log.', 'Today I feel happy!'),
('1', 20240523, 'calm', 'https://media1.giphy.com/media/FUORMziFnjV2tvAbPt/200w.mp4?cid=0303f60ashtpsucec3us1scxxit5nmk1rt2mgbxdr49lw8tv&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'Don’t waste your time in anger, regrets, worries, and grudges. Life is too short to be unhappy.', 'Zen!'),
('1', 20240522, 'frustrated', 'https://media4.giphy.com/media/xUNd9AWlNxNgnxiIxO/200w.mp4?cid=0303f60aw8n6rbf1tb5l49kgndy9ynu24ksk32rvhu477sdi&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'The most important thing is to enjoy your life—to be happy—its all that matters.', 'Super frustrated!'),
('1', 20240521, 'worried', 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTNwdDNhaW8xanRnM2JzcWVxb2V5M25jZnN1dGRjam5zZnc0bmF4aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUPJPzcdlbvaFUrF7y/giphy.mp4', 'Joke', 'What happens when you anger a brain surgeon? They will give you a piece of your mind.', 'I am worried!'),
('1', 20240520, 'angry', 'https://media2.giphy.com/media/7b5Wo64Jw53UI/200w.mp4?cid=0303f60arxkaehjyqbslmmb4gt7nqo503w9z4iags4fqze0k&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'What is this movie about? It is about 2 hours long.', 'GRRRR!'),
('1', 20240519, 'sad', 'https://media3.giphy.com/media/RIXdN6jjGtRd7dtIMC/200w.mp4?cid=0303f60aivbtq55ms46g8x2r7g2khant5gznuzmqzvkcmdh6&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'Why did the miner get fired from his job? He took it for granite...', 'Today I feel sad!'),
('1', 20240518, 'happy', 'https://media0.giphy.com/media/9tzXBdylmxKve/200w.mp4?cid=0303f60alvi8xdy3zog6n5giftaphhaji8f23jdf6z3i9ubr&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'I felt my lungs inflate with the onrush of scenery—air, mountains, trees, people. I thought, "This is what it is to be happy.', 'Today I feel happy!'),
('1', 20240517, 'calm', 'https://media1.giphy.com/media/FUORMziFnjV2tvAbPt/200w.mp4?cid=0303f60ashtpsucec3us1scxxit5nmk1rt2mgbxdr49lw8tv&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'Let us be grateful to the people who make us happy; they are the charming gardeners who make our souls blossom.', 'Zen!'),
('1', 20240516, 'happy', 'https://media0.giphy.com/media/9tzXBdylmxKve/200w.mp4?cid=0303f60alvi8xdy3zog6n5giftaphhaji8f23jdf6z3i9ubr&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'No medicine cures what happiness cannot.', 'Today I feel happy!'),
('1', 20240515, 'calm', 'https://media1.giphy.com/media/FUORMziFnjV2tvAbPt/200w.mp4?cid=0303f60ashtpsucec3us1scxxit5nmk1rt2mgbxdr49lw8tv&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'What kind of tree fits in your hand? A palm tree!', 'Zen!'),
('1', 20240514, 'angry', 'https://media2.giphy.com/media/7b5Wo64Jw53UI/200w.mp4?cid=0303f60arxkaehjyqbslmmb4gt7nqo503w9z4iags4fqze0k&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'If a child refuses to sleep during nap time, are they guilty of resisting a rest?', 'GRRRR!'),
('1', 20240513, 'angry', 'https://media2.giphy.com/media/7b5Wo64Jw53UI/200w.mp4?cid=0303f60arxkaehjyqbslmmb4gt7nqo503w9z4iags4fqze0k&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'If you want to be happy, do not dwell in the past, do not worry about the future, focus on living fully in the present.', 'GRRRR!'),
('1', 20240512, 'worried', 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTNwdDNhaW8xanRnM2JzcWVxb2V5M25jZnN1dGRjam5zZnc0bmF4aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUPJPzcdlbvaFUrF7y/giphy.mp4', 'Quote', 'Dreams are the touchstones of our characters.', 'I am worried!'),
('1', 20240511, 'worried', 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTNwdDNhaW8xanRnM2JzcWVxb2V5M25jZnN1dGRjam5zZnc0bmF4aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUPJPzcdlbvaFUrF7y/giphy.mp4', 'Joke', 'Why are graveyards so noisy? Because of all the coffin.', 'I am worried!'),
('1', 20240510, 'happy', 'https://media0.giphy.com/media/9tzXBdylmxKve/200w.mp4?cid=0303f60alvi8xdy3zog6n5giftaphhaji8f23jdf6z3i9ubr&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'In the news a courtroom artist was arrested today, I''m not surprised, he always seemed sketchy.', 'Today I feel happy!'),
('1', 20240509, 'calm', 'https://media1.giphy.com/media/FUORMziFnjV2tvAbPt/200w.mp4?cid=0303f60ashtpsucec3us1scxxit5nmk1rt2mgbxdr49lw8tv&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'What do you call a monkey in a mine field? A babooooom!', 'Zen!'),
('1', 20240508, 'calm', 'https://media1.giphy.com/media/FUORMziFnjV2tvAbPt/200w.mp4?cid=0303f60ashtpsucec3us1scxxit5nmk1rt2mgbxdr49lw8tv&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'Somebody stole my Microsoft Office and they''re going to pay - you have my Word.', 'Zen!'),
('1', 20240507, 'happy', 'https://media0.giphy.com/media/9tzXBdylmxKve/200w.mp4?cid=0303f60alvi8xdy3zog6n5giftaphhaji8f23jdf6z3i9ubr&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'Happiness is a warm puppy.', 'Today I feel happy!'),
('1', 20240506, 'calm', 'https://media1.giphy.com/media/FUORMziFnjV2tvAbPt/200w.mp4?cid=0303f60ashtpsucec3us1scxxit5nmk1rt2mgbxdr49lw8tv&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'Did you know you should always take an extra pair of pants golfing? Just in case you get a hole in one.', 'Zen!'),
('1', 20240505, 'calm', 'https://media1.giphy.com/media/FUORMziFnjV2tvAbPt/200w.mp4?cid=0303f60ashtpsucec3us1scxxit5nmk1rt2mgbxdr49lw8tv&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'It isnt what you have or who you are or where you are or what you are doing that makes you happy or unhappy. It is what you think about it.', 'Zen!'),
('1', 20240504, 'sad', 'https://media3.giphy.com/media/RIXdN6jjGtRd7dtIMC/200w.mp4?cid=0303f60aivbtq55ms46g8x2r7g2khant5gznuzmqzvkcmdh6&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'How many bones are in the human hand? A handful of them.', 'Today I feel sad!'),
('1', 20240503, 'frustrated', 'https://media4.giphy.com/media/xUNd9AWlNxNgnxiIxO/200w.mp4?cid=0303f60aw8n6rbf1tb5l49kgndy9ynu24ksk32rvhu477sdi&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'You cannot protect yourself from sadness without protecting yourself from happiness.', 'Super frustrated!'),
('1', 20240502, 'frustrated', 'https://media4.giphy.com/media/xUNd9AWlNxNgnxiIxO/200w.mp4?cid=0303f60aw8n6rbf1tb5l49kgndy9ynu24ksk32rvhu477sdi&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'How do you teach a kid to climb stairs? There is a step by step guide.', 'Super frustrated!'),
('1', 20240501, 'happy', 'https://media0.giphy.com/media/9tzXBdylmxKve/200w.mp4?cid=0303f60alvi8xdy3zog6n5giftaphhaji8f23jdf6z3i9ubr&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'I''ll tell you what often gets over looked... garden fences.', 'Today I feel happy!'),
('1', 20240601, 'happy', 'https://media0.giphy.com/media/9tzXBdylmxKve/200w.mp4?cid=0303f60alvi8xdy3zog6n5giftaphhaji8f23jdf6z3i9ubr&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'Where did you learn to make ice cream? Sunday school.', 'Today I feel happy!'),
('1', 20240602, 'frustrated', 'https://media4.giphy.com/media/xUNd9AWlNxNgnxiIxO/200w.mp4?cid=0303f60aw8n6rbf1tb5l49kgndy9ynu24ksk32rvhu477sdi&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'How do you teach a kid to climb stairs? There is a step by step guide.', 'Super frustrated!'),
('1', 20240603, 'frustrated', 'https://media4.giphy.com/media/xUNd9AWlNxNgnxiIxO/200w.mp4?cid=0303f60aw8n6rbf1tb5l49kgndy9ynu24ksk32rvhu477sdi&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'You cannot protect yourself from sadness without protecting yourself from happiness.', 'Super frustrated!'),
('1', 20240604, 'sad', 'https://media3.giphy.com/media/RIXdN6jjGtRd7dtIMC/200w.mp4?cid=0303f60aivbtq55ms46g8x2r7g2khant5gznuzmqzvkcmdh6&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'How many bones are in the human hand? A handful of them.', 'Today I feel sad!'),
('1', 20240605, 'calm', 'https://media1.giphy.com/media/FUORMziFnjV2tvAbPt/200w.mp4?cid=0303f60ashtpsucec3us1scxxit5nmk1rt2mgbxdr49lw8tv&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'It isnt what you have or who you are or where you are or what you are doing that makes you happy or unhappy. It is what you think about it.', 'Zen!'),
('1', 20240606, 'calm', 'https://media1.giphy.com/media/FUORMziFnjV2tvAbPt/200w.mp4?cid=0303f60ashtpsucec3us1scxxit5nmk1rt2mgbxdr49lw8tv&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'Did you know you should always take an extra pair of pants golfing? Just in case you get a hole in one.', 'Zen!'),
('1', 20240607, 'happy', 'https://media0.giphy.com/media/9tzXBdylmxKve/200w.mp4?cid=0303f60alvi8xdy3zog6n5giftaphhaji8f23jdf6z3i9ubr&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'Happiness is a warm puppy.', 'Today I feel happy!'),
('1', 20240608, 'calm', 'https://media1.giphy.com/media/FUORMziFnjV2tvAbPt/200w.mp4?cid=0303f60ashtpsucec3us1scxxit5nmk1rt2mgbxdr49lw8tv&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'Somebody stole my Microsoft Office and they''re going to pay - you have my Word.', 'Zen!'),
('1', 20240609, 'calm', 'https://media1.giphy.com/media/FUORMziFnjV2tvAbPt/200w.mp4?cid=0303f60ashtpsucec3us1scxxit5nmk1rt2mgbxdr49lw8tv&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'What do you call a monkey in a mine field? A babooooom!', 'Zen!'),
('1', 20240610, 'happy', 'https://media0.giphy.com/media/9tzXBdylmxKve/200w.mp4?cid=0303f60alvi8xdy3zog6n5giftaphhaji8f23jdf6z3i9ubr&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Joke', 'In the news a courtroom artist was arrested today, I''m not surprised, he always seemed sketchy.', 'Today I feel happy!'),
('1', 20240611, 'worried', 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTNwdDNhaW8xanRnM2JzcWVxb2V5M25jZnN1dGRjam5zZnc0bmF4aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUPJPzcdlbvaFUrF7y/giphy.mp4', 'Joke', 'Why are graveyards so noisy? Because of all the coffin.', 'I am worried!'),
('1', 20240612, 'worried', 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTNwdDNhaW8xanRnM2JzcWVxb2V5M25jZnN1dGRjam5zZnc0bmF4aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUPJPzcdlbvaFUrF7y/giphy.mp4', 'Quote', 'Dreams are the touchstones of our characters.', 'I am worried!'),
('1', 20240613, 'angry', 'https://media2.giphy.com/media/7b5Wo64Jw53UI/200w.mp4?cid=0303f60arxkaehjyqbslmmb4gt7nqo503w9z4iags4fqze0k&ep=v1_gifs_search&rid=200w.mp4&ct=g', 'Quote', 'If you want to be happy, do not dwell in the past, do not worry about the future, focus on living fully in the present.', 'GRRRR!');
