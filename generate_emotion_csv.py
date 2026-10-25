import csv
import os

data = [
    # JOY / POSITIVE
    ("emo_001", "I am so thrilled and grateful to have passed my final exams with distinction!", "joy", "positive", 0, "high"),
    ("emo_002", "Congratulations on your new promotion, you truly deserved this wonderful milestone!", "joy", "positive", 0, "high"),
    ("emo_003", "Spending this sunny afternoon with family in the park made my entire week so happy.", "joy", "positive", 0, "medium"),
    ("emo_004", "This is the best surprise gift I have ever received in my whole life! Thank you!", "joy", "positive", 0, "high"),
    ("emo_005", "Such a lovely and heartwarming story, it completely brightened my day.", "joy", "positive", 0, "medium"),
    ("emo_006", "We finally won the inter-college hackathon championship after 36 hours of coding!", "joy", "positive", 0, "high"),
    ("emo_007", "The puppy fell asleep right on my lap, my heart is totally melting right now.", "joy", "positive", 0, "high"),
    ("emo_008", "Eating delicious homemade pizza on a cozy Friday night is pure bliss.", "joy", "positive", 0, "medium"),
    ("emo_009", "Our research paper just got accepted for oral presentation at the conference!", "joy", "positive", 0, "high"),
    ("emo_010", "Grateful for good friends, good health, and another beautiful morning.", "joy", "positive", 0, "medium"),
    ("emo_011", "I can't stop smiling today, everything seems to be falling into place perfectly.", "joy", "positive", 0, "high"),
    ("emo_012", "Watching my sister walk across the stage at graduation brought tears of pure happiness.", "joy", "positive", 0, "high"),
    ("emo_013", "The concert last night was pure magic, the energy of the crowd was unreal!", "joy", "positive", 0, "high"),
    ("emo_014", "Finally booked our dream vacation to Switzerland, counting down the days!", "joy", "positive", 0, "high"),
    ("emo_015", "Woke up feeling refreshed, motivated, and excited for the new project.", "joy", "positive", 0, "medium"),

    # SADNESS / NEGATIVE
    ("emo_016", "I feel so lonely and exhausted, it feels like nothing I do ever works out.", "sadness", "negative", 0, "high"),
    ("emo_017", "Saying goodbye to my childhood pet today was the hardest thing I have ever had to do.", "sadness", "negative", 0, "high"),
    ("emo_018", "Miss my grandparents so much, wishing I could hug them just one more time.", "sadness", "negative", 0, "high"),
    ("emo_019", "Heartbroken after hearing the tragic news about our neighbor's family.", "sadness", "negative", 0, "high"),
    ("emo_020", "Put so much effort into this job interview only to receive a generic rejection email.", "sadness", "negative", 0, "medium"),
    ("emo_021", "Sitting alone in an empty room feeling like a complete disappointment to everyone.", "sadness", "negative", 0, "high"),
    ("emo_022", "It hurts when someone you trusted unconditionally suddenly treats you like a stranger.", "sadness", "negative", 0, "medium"),
    ("emo_023", "Rainy gloomy evening and all the old painful memories are rushing back.", "sadness", "negative", 0, "medium"),
    ("emo_024", "I hate feeling like an outsider no matter where I go or what group I join.", "sadness", "negative", 0, "medium"),
    ("emo_025", "Tired of putting on a fake smile when inside I am quietly falling apart.", "sadness", "negative", 0, "high"),
    ("emo_026", "Lost my notebook containing three years of handwritten poetry and memories.", "sadness", "negative", 0, "medium"),
    ("emo_027", "Another birthday spent alone in a new city away from my loved ones.", "sadness", "negative", 0, "medium"),
    ("emo_028", "The hospital visit confirmed my worst fears, feeling completely numb and broken.", "sadness", "negative", 0, "high"),
    ("emo_029", "It feels like everyone is moving forward in life while I am stuck in place.", "sadness", "negative", 0, "medium"),
    ("emo_030", "Grief doesn't disappear with time, it just changes shape and returns unexpectedly.", "sadness", "negative", 0, "high"),

    # ANGER / HOSTILITY / OFFENSIVE
    ("emo_031", "Shut up you absolute idiot, your stupid opinion is completely worthless garbage!", "anger", "negative", 1, "high"),
    ("emo_032", "You are a pathetic loser and a disgusting fraud, get lost and delete your account.", "anger", "negative", 1, "high"),
    ("emo_033", "I swear this airline has the most incompetent, useless staff on earth! Worst service ever!", "anger", "negative", 0, "high"),
    ("emo_034", "Look at this brainless clown pretending to know economics. You are a complete joke.", "anger", "negative", 1, "high"),
    ("emo_035", "Stop lying through your teeth, you greedy corrupt politicians make me so sick!", "anger", "negative", 0, "high"),
    ("emo_036", "Go back to your cave you ignorant creep, nobody wants your toxic hatred here.", "anger", "negative", 1, "high"),
    ("emo_037", "My package was stolen off my porch again! I am absolutely furious right now!", "anger", "negative", 0, "high"),
    ("emo_038", "You ruin everything you touch, just quit already you miserable failure.", "anger", "negative", 1, "high"),
    ("emo_039", "How dare you blame the victims when the administration's negligence caused this mess?!", "anger", "negative", 0, "high"),
    ("emo_040", "What a vile, disgusting excuse for a human being. Shame on you!", "anger", "negative", 1, "high"),
    ("emo_041", "Internet is down for the third time this week during an important exam! Ridiculous!", "anger", "negative", 0, "high"),
    ("emo_042", "Keep barking you dumb troll, nobody in this community respects your garbage takes.", "anger", "negative", 1, "high"),
    ("emo_043", "I hate dealing with hypocrites who preach morality but act with malicious selfishness.", "anger", "negative", 0, "medium"),
    ("emo_044", "You deserve all the hate and karma that is coming your way, you vile jerk.", "anger", "negative", 1, "high"),
    ("emo_045", "Total scam company! Stole my money and refused to respond to support tickets!", "anger", "negative", 0, "high"),

    # FEAR / ANXIETY
    ("emo_046", "My hands are shaking so badly, I am terrified of giving this presentation tomorrow.", "fear", "negative", 0, "high"),
    ("emo_047", "Heard strange scratching noises outside my window in the middle of the night.", "fear", "negative", 0, "high"),
    ("emo_048", "Panicking over the sudden chest pain, rushing to urgent care right now.", "fear", "negative", 0, "high"),
    ("emo_049", "The stock market crash wiped out half my savings, I don't know how I will survive.", "fear", "negative", 0, "high"),
    ("emo_050", "Terrified about the hurricane warning in our coastal district, boarding up windows.", "fear", "negative", 0, "high"),
    ("emo_051", "Waiting for biopsy test results is the most agonizing and scary waiting period.", "fear", "negative", 0, "high"),
    ("emo_052", "I have this deep, dreadful feeling that something terrible is about to happen.", "fear", "negative", 0, "medium"),
    ("emo_053", "Driving through dense fog on a mountain highway with zero visibility was frightening.", "fear", "negative", 0, "medium"),
    ("emo_054", "Scared of losing my scholarship if my GPA drops even by 0.1 points.", "fear", "negative", 0, "medium"),
    ("emo_055", "The sudden turbulence on our flight was so violent that passengers started praying aloud.", "fear", "negative", 0, "high"),
    ("emo_056", "Living in constant dread of an unexpected layoff in the tech sector.", "fear", "negative", 0, "medium"),
    ("emo_057", "Walked down a dark alley and heard footsteps closely following behind me.", "fear", "negative", 0, "high"),
    ("emo_058", "Worried sick about my mother who hasn't answered her phone all day.", "fear", "negative", 0, "high"),
    ("emo_059", "Terrified of failure and disappointing everyone who believed in me.", "fear", "negative", 0, "medium"),
    ("emo_060", "The doctor asked me to bring a family member for the follow-up, my stomach dropped.", "fear", "negative", 0, "high"),

    # SURPRISE
    ("emo_061", "Wait what?! I cannot believe they actually announced a sequel after 10 years!", "surprise", "positive", 0, "high"),
    ("emo_062", "Whoa, did not expect to run into my elementary school teacher at an airport in Tokyo!", "surprise", "positive", 0, "high"),
    ("emo_063", "I opened my mailbox and found an envelope stuffed with tickets to the World Cup finals!", "surprise", "positive", 0, "high"),
    ("emo_064", "Are you seriously telling me that this entire movie was filmed on a phone camera?!", "surprise", "neutral", 0, "medium"),
    ("emo_065", "Completely stunned by the unexpected plot twist in the final five minutes of the episode.", "surprise", "positive", 0, "high"),
    ("emo_066", "Never in a million years did I imagine our startup would hit 100,000 active users this fast!", "surprise", "positive", 0, "high"),
    ("emo_067", "Shocked to see snow falling in the desert this morning, nature is so unpredictable!", "surprise", "neutral", 0, "high"),
    ("emo_068", "My dog actually learned how to turn the door handle and let himself into the kitchen!", "surprise", "positive", 0, "medium"),
    ("emo_069", "Wait, you're telling me tomorrow is already the deadline?! Time flew by so fast!", "surprise", "negative", 0, "medium"),
    ("emo_070", "I genuinely did not expect this budget smartphone camera to produce such sharp portraits.", "surprise", "positive", 0, "medium"),

    # DISGUST
    ("emo_071", "Found a dead cockroach inside my restaurant soup bowl, absolutely revolting and gross!", "disgust", "negative", 0, "high"),
    ("emo_072", "The public restroom at the bus terminal was unimaginably filthy and smelled sickening.", "disgust", "negative", 0, "high"),
    ("emo_073", "Such a toxic, vile predator using fake charity accounts to scam elderly people.", "disgust", "negative", 1, "high"),
    ("emo_074", "I feel sick to my stomach watching these corporate executives celebrate worker layoffs.", "disgust", "negative", 0, "high"),
    ("emo_075", "The kitchen sink was overflowing with greasy sludge, could barely stand the stench.", "disgust", "negative", 0, "medium"),
    ("emo_076", "What a slimy, deceitful scumbag who betrays his own teammates behind their backs.", "disgust", "negative", 1, "high"),
    ("emo_077", "Opening stale milk that expired two weeks ago was a horrific sensory assault.", "disgust", "negative", 0, "medium"),
    ("emo_078", "Disgusted by the sheer amount of plastic garbage dumped along this beautiful coral reef.", "disgust", "negative", 0, "high"),
    ("emo_079", "Watching corrupt judges let off criminals because of political ties makes my blood boil with disgust.", "disgust", "negative", 0, "high"),
    ("emo_080", "You are the most hypocritical degenerate on the internet, absolute trash human.", "disgust", "negative", 1, "high"),

    # NEUTRAL / INFORMATIVE
    ("emo_081", "The library opens at 8:00 AM on weekdays and closes at 9:00 PM on Saturdays.", "neutral", "neutral", 0, "low"),
    ("emo_082", "Please remember to submit your weekly progress report before Friday 5:00 PM.", "neutral", "neutral", 0, "low"),
    ("emo_083", "According to meteorological data, tomorrow's temperature will hover around 22 degrees Celsius.", "neutral", "neutral", 0, "low"),
    ("emo_084", "The seminar will cover recent developments in transformer self-attention mechanisms.", "neutral", "neutral", 0, "low"),
    ("emo_085", "Train number 12431 departs from platform 4 at 14:30 hours with an expected 10-minute delay.", "neutral", "neutral", 0, "low"),
    ("emo_086", "Could you please email me the updated spreadsheet containing the customer feedback records?", "neutral", "neutral", 0, "low"),
    ("emo_087", "The algorithm uses stochastic gradient descent with an initial learning rate of 0.001.", "neutral", "neutral", 0, "low"),
    ("emo_088", "Coffee beans should ideally be stored in an airtight container away from direct sunlight.", "neutral", "neutral", 0, "low"),
    ("emo_089", "Registration for the annual athletic championship is open until the end of this month.", "neutral", "neutral", 0, "low"),
    ("emo_090", "The system architecture diagram has been uploaded to the shared team repository folder.", "neutral", "neutral", 0, "low"),
    ("emo_091", "Python 3.11 introduced substantial performance improvements including specialized adaptive bytecode.", "neutral", "neutral", 0, "low"),
    ("emo_092", "The college bus route covers five major zones starting from the northern terminus.", "neutral", "neutral", 0, "low"),
    ("emo_093", "Please verify your email address to complete the two-factor authentication setup.", "neutral", "neutral", 0, "low"),
    ("emo_094", "The university cafeteria menu offers vegetarian and vegan meal options daily.", "neutral", "neutral", 0, "low"),
    ("emo_095", "Our laboratory is equipped with high-performance computing clusters and GPU acceleration.", "neutral", "neutral", 0, "low"),

    # NUANCED & SLANG / COLLOQUIAL (HARMLESS VS OFFENSIVE)
    ("emo_096", "Damn, this chocolate lava cake is ridiculously good!", "joy", "positive", 0, "high"),
    ("emo_097", "Holy cow, that guitar solo in the bridge was completely insane!", "surprise", "positive", 0, "high"),
    ("emo_098", "Oh wow, another absolute genius blessing us with their boundless wisdom. Such a clown.", "anger", "negative", 1, "medium"),
    ("emo_099", "I am dead laughing right now, this cat video made my entire week!", "joy", "positive", 0, "high"),
    ("emo_100", "Get lost you stupid idiot and stop spamming your worthless garbage here.", "anger", "negative", 1, "high")
]

file_path = os.path.join(os.path.dirname(__file__), "social_media_emotion_dataset.csv")

with open(file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "text", "emotion", "sentiment", "offensive_label", "intensity"])
    for row in data:
        writer.writerow(row)

print(f"Generated {len(data)} rows in {file_path}")
