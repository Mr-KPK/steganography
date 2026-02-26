*Encoding Flow*

User chooses 1
        ↓
Enter image path
        ↓
Enter secret message
        ↓
Convert message → Binary
        ↓
Add delimiter
        ↓
Open image
        ↓
Replace LSB of RGB pixels
        ↓
Save new image
        ↓
Message encoded successfully



*Decoding Flow*

User chooses 2
        ↓
Open encoded image
        ↓
Extract LSB from all pixels
        ↓
Combine into binary string
        ↓
Stop at delimiter
        ↓
Convert binary → text
        ↓
Print hidden message
