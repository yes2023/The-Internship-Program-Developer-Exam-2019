# Hangman

## Contact
ชื่อ: ภัคพงศ์ อัตถวิบูลย์

Name: Pakkapong Attawiboon

Email: pakkapong.att@mail.kmutt.ac.th

Tel: 0855431180

## System requirements
Python 3.7.2

## Instruction
To run the program

```bash
py hangman.py
```

If you want to add more quiz just add .json file into Quiz folder with the format below

ถ้าหากต้องการเพิ่ม Quiz ให้ทำการเพิ่มไฟล์ .json ลงในโฟลเดอร์  Quiz โดยไฟล์ json ให้ทำตาม format ดังนี้

```json
{
  "Category": "Exmaple",
  "quiz": [
    {
      "hint": "Fortune Cookies",
      "answer": "BNK48!!"
    },
    {
      "hint": "Hotel California",
      "answer": "The Eagles"
    },
  ]
}
```