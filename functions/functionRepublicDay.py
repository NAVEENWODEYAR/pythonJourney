# ============================================================
# 🇮🇳 HAPPY REPUBLIC DAY 🇮🇳
# India - Republic Day Information Program
# ============================================================

from datetime import date

# ------------------------------------------------------------
# CURRENT YEAR
# ------------------------------------------------------------

current_year = date.today().year

# Republic Day started in 1950
first_republic_day = 1950

republic_day_number = current_year - first_republic_day + 1


# ------------------------------------------------------------
# WELCOME MESSAGE
# ------------------------------------------------------------

print("\n")
print("=" * 65)
print("🇮🇳🇮🇳🇮🇳       HAPPY REPUBLIC DAY       🇮🇳🇮🇳🇮🇳")
print("=" * 65)

print("\nWelcome to the Republic Day Information Program!")
print("Let us learn about the history and people behind our Constitution.\n")


# ------------------------------------------------------------
# BASIC INFORMATION
# ------------------------------------------------------------

print("=" * 65)
print("📚 BASIC INFORMATION")
print("=" * 65)

print("🇮🇳 Country              : India")
print("📅 Republic Day         : 26 January")
print("🎉 First Republic Day   : 26 January 1950")
print("📜 Constitution Adopted : 26 November 1949")
print("📜 Constitution Enforced: 26 January 1950")
print("🎊 Current Republic Day : " + str(republic_day_number) + "th Republic Day")


# ------------------------------------------------------------
# WHY DO WE CELEBRATE REPUBLIC DAY?
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("❓ WHY DO WE CELEBRATE REPUBLIC DAY?")
print("=" * 65)

print("""
India became independent on 15 August 1947.

However, India still needed its own Constitution
to define how the country would be governed.

The Constitution of India was adopted on
26 November 1949.

It came into force on 26 January 1950.

On that day, India became a Sovereign Democratic Republic.

Therefore, 26 January is celebrated every year as
REPUBLIC DAY.
""")


# ------------------------------------------------------------
# WHY 26 JANUARY?
# ------------------------------------------------------------

print("=" * 65)
print("📅 WHY WAS 26 JANUARY CHOSEN?")
print("=" * 65)

print("""
26 January has an important connection with India's
freedom movement.

On 26 January 1930, Purna Swaraj (Complete Independence)
was observed as a national objective.

When the Constitution was brought into force in 1950,
26 January was deliberately chosen to honour this
historical connection.
""")


# ------------------------------------------------------------
# CONSTITUENT ASSEMBLY
# ------------------------------------------------------------

print("=" * 65)
print("🏛️ CONSTITUENT ASSEMBLY")
print("=" * 65)

print("""
The Constituent Assembly was responsible for preparing
the Constitution of India.

The Assembly worked for nearly three years.

Important dates:

9 December 1946
→ First sitting of the Constituent Assembly

29 August 1947
→ Drafting Committee was appointed

26 November 1949
→ Constitution was adopted

24 January 1950
→ Members signed the Constitution

26 January 1950
→ Constitution came into force
""")


# ------------------------------------------------------------
# MAIN PERSONALITIES
# ------------------------------------------------------------

print("=" * 65)
print("👨‍⚖️ MAIN PERSONALITIES")
print("=" * 65)

print("""
1. Dr. B. R. Ambedkar
   → Chairman of the Drafting Committee
   → One of the principal architects of the Constitution

2. Dr. Rajendra Prasad
   → President of the Constituent Assembly
   → Became the first President of India

3. Jawaharlal Nehru
   → First Prime Minister of independent India
   → Moved the Objectives Resolution in the Constituent Assembly

4. Sardar Vallabhbhai Patel
   → Important member of the Constituent Assembly
   → Played a major role in committees dealing with
     fundamental rights and other constitutional matters

5. B. N. Rau
   → Constitutional Adviser to the Constituent Assembly
   → Played an important role in preparing constitutional drafts

6. K. M. Munshi
   → Member of the Drafting Committee
   → Important contributor to constitutional discussions

7. Alladi Krishnaswami Ayyar
   → Member of the Drafting Committee
   → Distinguished lawyer and constitutional contributor

8. N. Gopalaswami Ayyangar
   → Member of the Drafting Committee
   → Important contributor to constitutional work

9. Mohammad Saadulla
   → Member of the Drafting Committee

10. B. L. Mitter
    → Original member of the Drafting Committee

11. D. P. Khaitan
    → Original member of the Drafting Committee
""")


# ------------------------------------------------------------
# DRAFTING COMMITTEE
# ------------------------------------------------------------

print("=" * 65)
print("📝 DRAFTING COMMITTEE")
print("=" * 65)

print("""
The Drafting Committee was appointed on 29 August 1947.

Chairman:
→ Dr. B. R. Ambedkar

Important members included:

→ Dr. B. R. Ambedkar
→ N. Gopalaswami Ayyangar
→ Alladi Krishnaswami Ayyar
→ K. M. Munshi
→ Mohammad Saadulla
→ B. L. Mitter
→ D. P. Khaitan

Some members were later replaced because of resignation
or death.
""")


# ------------------------------------------------------------
# IMPORTANT DATES
# ------------------------------------------------------------

print("=" * 65)
print("📜 IMPORTANT DATES")
print("=" * 65)

events = {
    1930: "26 January - Purna Swaraj Day was observed",
    1946: "9 December - First sitting of the Constituent Assembly",
    1947: "15 August - India became independent",
    1947: "29 August - Drafting Committee was appointed",
    1949: "26 November - Constitution was adopted",
    1950: "24 January - Members signed the Constitution",
    1950: "26 January - Constitution came into force"
}

for year, event in events.items():
    print(str(year) + " → " + event)


# ------------------------------------------------------------
# VALUES OF THE CONSTITUTION
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("⚖️ VALUES OF THE CONSTITUTION")
print("=" * 65)

print("""
The Preamble highlights important ideals such as:

⚖️ Justice
🕊️ Liberty
🤝 Equality
❤️ Fraternity

These values form an important part of India's
constitutional vision.
""")


# ------------------------------------------------------------
# REPUBLIC DAY CELEBRATION
# ------------------------------------------------------------

print("=" * 65)
print("🎖️ HOW IS REPUBLIC DAY CELEBRATED?")
print("=" * 65)

print("""
🇮🇳 Flag ceremonies
🎖️ Military parade
🥁 Cultural performances
🏫 School and college programmes
🏆 Awards and honours
✈️ Military and cultural displays
🎭 Tableaux representing different parts of India

The main national celebration takes place in New Delhi.
""")


# ------------------------------------------------------------
# REPUBLIC DAY COUNT
# ------------------------------------------------------------

print("=" * 65)
print("🎊 REPUBLIC DAY COUNT")
print("=" * 65)

print("Current Year          :", current_year)
print("First Republic Day    : 1950")
print("Republic Day Number   :", republic_day_number)

if current_year == 2026:
    print("🇮🇳 2026 is India's 77th Republic Day! 🇮🇳")


# ------------------------------------------------------------
# FINAL MESSAGE
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("🇮🇳🇮🇳🇮🇳       HAPPY REPUBLIC DAY       🇮🇳🇮🇳🇮🇳")
print("=" * 65)

print("""
Let us remember the great leaders and citizens
who helped build our democratic nation.

Let us respect our Constitution,
our democracy and our country.

        🇮🇳 JAI HIND! 🇮🇳
        🇮🇳 VANDE MATARAM! 🇮🇳
        🇮🇳 HAPPY REPUBLIC DAY! 🇮🇳
""")

print("=" * 65)