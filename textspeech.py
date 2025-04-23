from gtts import gTTS
import os
import time
txt="Welcome to the Story Time.THE TWO LITTLE GIRLS. The Two Little Girls is a heartwarming story about Alle and Alice. Two sisters from Male,the capital city of the Maldives, each grappling with their own fears-Alle with darkness and solitude,and Alice with a sea. Their parents concerned about their daughters anxieties,decide that confronting these fears head-on is the best solution.  Alice's journey begins when her father arranges for her to attend school in the United States,a decision that requires a boat voyage from the Maldives. Despite her initial terror of the sea,Alice faces the challenge,especially when a violent storm tests her courage. Her prayers for safety are answered,reinforcing her faith and diminishing her fear.Back home, Alle confronts her fear of the dark when a power outage leaves her alone at night. Choosing to sleep on the sofa, she experiences a series of unsettling events that ultimately empower her to face her bedroom alone, overcoming her fear.The story concludes with both sisters returning home, transformed by their experiences,no longer fearful of the sea or the dark. The moral emphasizes trusting in God's constant presence and protection, echoing the sentiment from Joshua 1:9 Have I not commanded you? Be strong and courageous. Do not be frightened, and do not be dismayed, for the Lord your God is with you wherever you go. This narrative beautifully illustrates how facing one's fears with faith can lead to personal growth and a deeper sense of security."
lang="en"
x=gTTS(text=txt,lang=lang,slow=False)
x.save("welcome.mp3")
os.system("start welcome.mp3")







