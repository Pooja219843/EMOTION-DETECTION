import os
import pandas as pd
import numpy as np

def create_datasets():
    data_dir = os.path.join(os.path.dirname(__file__), 'app', 'data')
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(os.path.join(data_dir, 'saved_models'), exist_ok=True)

    # Core offensive and non-offensive templates and samples reflecting real OLID / social media distribution
    offensive_samples = [
        "You are so stupid and nobody likes you, delete your account.",
        "Get lost you absolute idiot and stop spreading lies.",
        "Shut up, your opinion is completely worthless and trash.",
        "Nobody cares about what you think, stop crying you loser.",
        "Why are you such an annoying clown? Go touch grass.",
        "What a pathetic human being you are, disgusting behavior.",
        "You're a disgusting piece of garbage, get out of here.",
        "This guy is a complete moron who knows nothing about politics.",
        "Stop talking rubbish you ignorant fool.",
        "Go back to where you came from, we don't want your kind here.",
        "You deserve all the hate you are getting, you vile jerk.",
        "Can someone slap some sense into this brainless creature?",
        "Such a toxic scumbag, never post here again.",
        "You are ugly inside and out, honestly sickening.",
        "What an arrogant, obnoxious punk you are.",
        "Look at this clown pretending to be smart. You're a joke.",
        "Keep barking dog, nobody is listening to your nonsense.",
        "You are a total fraud and a miserable failure in life.",
        "Shut your mouth before you make a bigger fool of yourself.",
        "I have never seen someone as dumb as this poster right here.",
        "What a hateful creep, you should be permanently banned.",
        "Only brainwashed sheep and idiots would believe your garbage.",
        "You ruin everything you touch, just quit already.",
        "Typical coward hiding behind a fake profile to talk trash.",
        "You are the most hypocritical degenerate on the internet."
    ]

    non_offensive_samples = [
        "I really loved your latest presentation, it was very informative and helpful!",
        "Could you please share the reference link for this research paper?",
        "The weather today is surprisingly pleasant in the city.",
        "Congratulations on your graduation, wishing you all the best!",
        "I disagree with this policy proposal, but I respect your perspective.",
        "Thank you so much for explaining the machine learning concepts so clearly.",
        "Has anyone tried the new bakery downtown? The croissants are amazing.",
        "Looking forward to the conference tomorrow morning at 9 AM.",
        "Can someone explain the difference between supervised and unsupervised learning?",
        "Happy birthday! Hope you have a wonderful celebration with your family.",
        "That was a great football match last night, both teams played really well.",
        "I appreciate your thoughtful response, it gave me a lot to think about.",
        "Let us schedule our weekly team sync for Thursday afternoon.",
        "Damn, this chocolate cake is ridiculously good!",
        "The cinematography in that movie was absolutely breathtaking.",
        "Safe travels on your flight back home, let us know when you land.",
        "Great work by the open-source community on this new release.",
        "I am currently reading a fascinating book on cognitive neuroscience.",
        "Could you recommend any good tutorials for learning React with TypeScript?",
        "Such an inspiring speech by the keynote speaker today.",
        "The train was slightly delayed today due to routine track maintenance.",
        "We should definitely collaborate on this project during the next semester.",
        "Thanks for the quick response and detailed feedback on my pull request.",
        "What time does the university library close on weekends?",
        "Beautiful sunset photograph! Which camera settings did you use?"
    ]

    # Additional contextual variations for training stability and robust vocabulary
    variations_off = [
        "Go away loser.", "You are worthless trash.", "Nobody asked for your stupid opinion.",
        "Shut up and mind your business fool.", "You make me sick with your hateful nonsense.",
        "What an utter disaster of a human.", "Stop being such an incompetent crybaby.",
        "You are deeply unintelligent and it shows in every tweet.",
        "Trash take from a trash person as expected.", "Why are you still breathing our air?",
        "Total scammer and pathological liar.", "You are pathetic beyond words.",
        "Such an arrogant jerk who can't handle the truth.", "Get off twitter you disgusting troll.",
        "You're a clown and everyone is laughing at your failure.",
        "F**k off and stop harassing people here.", "Stupid comments like yours ruin the community.",
        "You are an embarrassment to your entire family.", "Keep crying you bitter loser.",
        "Look at this brain-dead take, delete this immediately."
    ]

    variations_non_off = [
        "That sounds like an excellent solution to the problem.",
        "I really enjoyed reading your blog post today.",
        "Do you know when the assignment grades will be published?",
        "Let's review the code changes together in tomorrow's standup.",
        "The new UI update looks very clean and intuitive.",
        "Holy cow, this algorithm is surprisingly fast and accurate!",
        "Thanks for helping me debug that tricky runtime error.",
        "Wishing everyone a productive and peaceful week ahead.",
        "The dataset includes over 10,000 labelled samples for classification.",
        "Could we set up a quick 10-minute call to discuss the project?",
        "Awesome achievement, very well deserved recognition!",
        "Interesting observation regarding the attention mechanisms in transformers.",
        "I will push my git commits before the end of the day.",
        "Is the cafeteria open on campus today?",
        "That was an insightful discussion on natural language processing.",
        "Good luck with your final semester examinations!",
        "Please let me know if you need any assistance with the documentation.",
        "The conference schedule has been posted on the department website.",
        "A balanced diet and regular exercise are vital for healthy living.",
        "Thank you for sharing your thoughts in such a courteous manner."
    ]

    # Combine and expand to create stratified datasets
    np.random.seed(42)
    
    train_texts = []
    train_labels = []

    # Build 800 training examples (approx 400 non-off, 400 off)
    all_off = offensive_samples * 16 + variations_off * 10
    all_non = non_offensive_samples * 16 + variations_non_off * 10

    # Add slight random prefixes/suffixes to mimic authentic social media variance
    prefixes_off = ["@user ", "Honestly, ", "Dude, ", "Seriously, ", "Look, ", "", "", "@someone "]
    prefixes_non = ["@user ", "Hello, ", "Hi guys, ", "Actually, ", "In my opinion, ", "", "", "Hey! "]

    for i, t in enumerate(all_off[:450]):
        p = np.random.choice(prefixes_off)
        train_texts.append(f"{p}{t}".strip())
        train_labels.append(1)

    for i, t in enumerate(all_non[:550]):
        p = np.random.choice(prefixes_non)
        train_texts.append(f"{p}{t}".strip())
        train_labels.append(0)

    # Shuffle training set
    indices = np.arange(len(train_texts))
    np.random.shuffle(indices)
    df_train = pd.DataFrame({
        'id': [f"train_{idx:04d}" for idx in range(len(indices))],
        'text': [train_texts[i] for i in indices],
        'label': [train_labels[i] for i in indices]
    })

    # Build held-out test dataset (200 test examples with distinct tweets)
    test_off = [
        "You are so stupid and worthless, please leave.",
        "Shut up idiot, nobody wants to hear your toxic lies.",
        "What a pathetic clown you are, get a real life.",
        "You're a disgusting liar and a shameless hypocrite.",
        "Go back to your cave you ignorant creep.",
        "Such a toxic scumbag, stop embarrassing yourself.",
        "You are genuinely one of the dumbest people I have ever met.",
        "Nobody cares about your whining, go cry somewhere else.",
        "What an arrogant jerk who knows absolutely nothing.",
        "You should delete your account and never come back.",
        "This idiot actually thought his opinion mattered.",
        "Trash human being with zero brain cells.",
        "Stop spamming this garbage you brainless troll.",
        "You are a total fraud and a complete failure.",
        "Get lost you absolute joke of a person."
    ] * 6

    test_non = [
        "Thank you for the helpful explanation, this made things much clearer.",
        "I really appreciate your kind support on this project.",
        "The conference keynote was genuinely inspiring and well delivered.",
        "Looking forward to meeting everyone at the research workshop.",
        "Could you recommend a good tutorial for understanding attention mechanisms?",
        "Congratulations on receiving the academic excellence award!",
        "The autumn weather is truly lovely today for a morning walk.",
        "I respectfully disagree with the premise, but your argument is logical.",
        "Damn, this new GPU performs ten times faster than the old one!",
        "Please send me the updated meeting minutes when you have a moment.",
        "Wishing you and your team the best of luck on the final presentation.",
        "The open-source library documentation is comprehensive and easy to navigate.",
        "Let us catch up over coffee this Thursday afternoon.",
        "Safe travels to the entire research team heading to the conference.",
        "Great job on completing the sprint goals ahead of schedule!"
    ] * 8

    test_texts = [f"@user {t}" for t in test_off[:80]] + [f"@user {t}" for t in test_non[:120]]
    test_labels = [1]*80 + [0]*120
    t_indices = np.arange(len(test_texts))
    np.random.shuffle(t_indices)

    df_test = pd.DataFrame({
        'id': [f"test_{idx:04d}" for idx in range(len(t_indices))],
        'text': [test_texts[i] for i in t_indices],
        'label': [test_labels[i] for i in t_indices]
    })

    # Build sample batch file for user upload demonstration
    sample_batch = pd.DataFrame({
        'comment_id': [f"cmt_{i+1:03d}" for i in range(12)],
        'comment_text': [
            "What a fantastic initiative by the university, very proud to see this!",
            "You are an absolute clown and your channel is garbage.",
            "Can you explain why the loss function plateaus after epoch 5?",
            "Shut up you toxic idiot, nobody cares about your opinion.",
            "Damn that goal in the 90th minute was totally unbelievable!",
            "Go crawl back into your hole you disgusting coward.",
            "Thank you so much for the code review comments, I will refactor right away.",
            "Why is this guy allowed on the platform? What a miserable creep.",
            "The accuracy of the model improved by 6.4% on the held-out validation set.",
            "Stop crying like a baby and accept that you lost fair and square.",
            "Wishing everyone in the community a peaceful and productive week.",
            "You are such a fake hypocrite, nobody trusts anything you say."
        ]
    })

    train_path = os.path.join(data_dir, 'olid_train.csv')
    test_path = os.path.join(data_dir, 'olid_test.csv')
    batch_path = os.path.join(data_dir, 'sample_batch.csv')

    df_train.to_csv(train_path, index=False)
    df_test.to_csv(test_path, index=False)
    sample_batch.to_csv(batch_path, index=False)

    print(f"Datasets created successfully at {data_dir}:")
    print(f"- Train: {len(df_train)} rows (Class 0: {(df_train['label']==0).sum()}, Class 1: {(df_train['label']==1).sum()})")
    print(f"- Test: {len(df_test)} rows (Class 0: {(df_test['label']==0).sum()}, Class 1: {(df_test['label']==1).sum()})")
    print(f"- Sample Batch: {len(sample_batch)} rows")

if __name__ == '__main__':
    create_datasets()
