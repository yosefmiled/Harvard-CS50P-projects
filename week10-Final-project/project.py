import os
import sys
from dotenv import load_dotenv
from google import genai

from rich.console import Console
from rich import box
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_african_countries():
    return [
        ("Algeria", "🇩🇿", "North Africa"),
        ("Angola", "🇦🇴", "Central Africa"),
        ("Benin", "🇧🇯", "West Africa"),
        ("Botswana", "🇧🇼", "Southern Africa"),
        ("Burkina Faso", "🇧🇫", "West Africa"),
        ("Burundi", "🇧🇮", "East Africa"),
        ("Cabo Verde", "🇨🇻", "West Africa"),
        ("Cameroon", "🇨🇲", "Central Africa"),
        ("Central African Republic", "🇨🇫", "Central Africa"),
        ("Chad", "🇹🇩", "Central Africa"),
        ("Comoros", "🇰🇲", "East Africa"),
        ("Congo (Brazzaville)", "🇨🇬", "Central Africa"),
        ("Congo (Kinshasa)", "🇨🇩", "Central Africa"),
        ("Djibouti", "🇩🇯", "East Africa"),
        ("Egypt", "🇪🇬", "North Africa"),
        ("Equatorial Guinea", "🇬🇶", "Central Africa"),
        ("Eritrea", "🇪🇷", "East Africa"),
        ("Eswatini", "🇸🇿", "Southern Africa"),
        ("Ethiopia", "🇪🇹", "East Africa"),
        ("Gabon", "🇬🇦", "Central Africa"),
        ("Gambia", "🇬🇲", "West Africa"),
        ("Ghana", "🇬🇭", "West Africa"),
        ("Guinea", "🇬🇳", "West Africa"),
        ("Guinea-Bissau", "🇬🇼", "West Africa"),
        ("Ivory Coast", "🇨🇮", "West Africa"),
        ("Kenya", "🇰🇪", "East Africa"),
        ("Lesotho", "🇱🇸", "Southern Africa"),
        ("Liberia", "🇱🇷", "West Africa"),
        ("Libya", "🇱🇾", "North Africa"),
        ("Madagascar", "🇲🇬", "East Africa"),
        ("Malawi", "🇲🇼", "East Africa"),
        ("Mali", "🇲🇱", "West Africa"),
        ("Mauritania", "🇲🇷", "North Africa"),
        ("Mauritius", "🇲🇺", "East Africa"),
        ("Morocco", "🇲🇦", "North Africa"),
        ("Mozambique", "🇲🇿", "Southern Africa"),
        ("Namibia", "🇳🇦", "Southern Africa"),
        ("Niger", "🇳🇪", "West Africa"),
        ("Nigeria", "🇳🇬", "West Africa"),
        ("Rwanda", "🇷🇼", "East Africa"),
        ("Sao Tome & Principe", "🇸🇹", "Central Africa"),
        ("Senegal", "🇸🇳", "West Africa"),
        ("Seychelles", "🇸🇨", "East Africa"),
        ("Sierra Leone", "🇸🇱", "West Africa"),
        ("Somalia", "🇸🇴", "East Africa"),
        ("South Africa", "🇿🇦", "Southern Africa"),
        ("South Sudan", "🇸🇸", "East Africa"),
        ("Sudan", "🇸🇩", "North Africa"),
        ("Tanzania", "🇹🇿", "East Africa"),
        ("Togo", "🇹🇬", "West Africa"),
        ("Tunisia", "🇹🇳", "North Africa"),
        ("Uganda", "🇺🇬", "East Africa"),
        ("Zambia", "🇿🇲", "Southern Africa"),
        ("Zimbabwe", "🇿🇼", "Southern Africa"),
    ]

history = {
    "label": "🏛️  History",
    "key": "History",
    "subs": [
        "Ancient History",
        "Colonial History",
        "Independence & Modern Politics",
        "Language History",
        "Ethnic & Tribal History",
    ],
}

food = {
    "label": "🍲  Food & Recipes",
    "key": "Food & Recipes",
    "subs": [
        "Food Culture Overview",
        "National Dishes",
        "A Traditional Recipe",
    ],
}

languages = {
    "label": "🌐  Languages & Dialects",
    "key": "Languages & Dialects",
    "subs": [
        "Official Languages",
        "Regional Dialects",
        "Common Phrases to Learn",
    ],
}

famous_people = {
    "label": "⚽  Famous People & Athletes",
    "key": "Famous People & Athletes",
    "subs": [
        "Historical Figures",
        "Politicians & Leaders",
        "Athletes",
        "Artists & Musicians",
    ],
}

CATEGORIES = {
    "1": history,
    "2": food,
    "3": languages,
    "4": famous_people,
}

def validate(num, range):
    if not num.strip().isdigit():
        return False
    return 1 <= int(num.strip()) <= range

def prompt(country, category, subcategory):
    if category == "History":
        if subcategory == "Ancient History":
            return f"Give a rich overview of the ancient history of {country}. Include major civilizations, kingdoms, or empires. 3-4 paragraphs."
        elif subcategory == "Colonial History":
            return f"Describe the colonial history of {country}. Which powers colonized it, when, and what was the lasting impact? 3-4 paragraphs."
        elif subcategory == "Independence & Modern Politics":
            return f"Explain {country}'s path to independence and modern political history. Include key leaders and turning points. 3-4 paragraphs."
        elif subcategory == "Language History":
            return f"Describe the history of languages in {country}, including indigenous languages and colonial influences. 3-4 paragraphs."
        elif subcategory == "Ethnic & Tribal History":
            return f"Give an overview of the main ethnic groups and tribes in {country}, their origins and historical relationships. 3-4 paragraphs."

    elif category == "Food & Recipes":
        if subcategory == "Food Culture Overview":
            return f"Describe the food culture of {country}. Staple ingredients, cooking styles, and cultural significance. 3-4 paragraphs."
        elif subcategory == "National Dishes":
            return f"List and describe the 6 most iconic national dishes of {country}. For each: name, description, and key ingredients."
        elif subcategory == "A Traditional Recipe":
            return f"Give a complete authentic traditional recipe from {country}. Include ingredients with quantities and step-by-step instructions."

    elif category == "Languages & Dialects":
        if subcategory == "Official Languages":
            return f"Describe the official languages of {country}, their history and everyday usage. 3 paragraphs."
        elif subcategory == "Regional Dialects":
            return f"Describe the main regional dialects and local languages spoken across {country}. 3 paragraphs."
        elif subcategory == "Common Phrases to Learn":
            return f"Give 10 useful everyday phrases in the most widely spoken local language of {country}. For each: the phrase, pronunciation, and English meaning."

    elif category == "Famous People & Athletes":
        if subcategory == "Historical Figures":
            return f"Describe 5 of the most important historical figures from {country}. Include their era, role, and legacy."
        elif subcategory == "Politicians & Leaders":
            return f"Describe 5 notable politicians and leaders from {country}. Include their era and impact."
        elif subcategory == "Athletes":
            return f"Name and describe 5 of the most famous athletes from {country}. Include their sport and greatest achievements."
        elif subcategory == "Artists & Musicians":
            return f"Name and describe 5 famous artists and musicians from {country}. Include their medium and cultural impact."

    return f"Tell me about {subcategory} in {country} in 3-4 informative paragraphs."

def format_response(text):
    if not text :
        return ""
    lines = text.strip().split("/n")
    cleaned = []
    prev_blank = False
    for line in lines :
        if line.strip() == "":
            if not prev_blank :
                cleaned.append(line)
            prev_blank = True
        else :
            cleaned.append(line)
            prev_blank = False

    return "/n".join(cleaned)

def ai_response(p):
    try:
        response = client.models.generate_content(model="gemini-2.5-flash",contents=p + " Do not use any markdown formatting in your response.")
        return response.text
    except Exception as e :
        return f"Error: {e}"

def display_country_table():
    countries = get_african_countries()
    table = Table(title="🌍  African Countries", box=box.ROUNDED, border_style="yellow", show_lines=True)
    table.add_column("No.", style="bold cyan", width=5, justify="right")
    table.add_column("Flag", width=5)
    table.add_column("Country", style="bold white")
    table.add_column("Region", style="dim green")
    for i, (name,flag,region) in enumerate(countries, 1):
        table.add_row(str(i), flag, name, region)
    console.print(table)
    return countries

def display_menu(title, options, border="cyan"):
    table = Table(title=title, box=box.ROUNDED, border_style="yellow", show_lines=True)
    table.add_column("No.", style="bold cyan", width=5, justify="right")
    table.add_column("options", style="bold white")

    for i, options in enumerate(options, 1):
        table.add_row(str(i), options)
    table.add_row("[dim]B[/dim]", "[dim]  Back[/dim]")
    table.add_row("[dim]Q[/dim]", "[dim]  Quit[/dim]")
    console.print(table)

def main():
    console.print(Panel(
        "Welcome to Explore Africa!/n/n"
        "An AI-powered interactive guide to African cultures,/n"
        "history, food, languages, and more./n/n"
        "Covering all 54 African countries",
        border_style="green",
        padding=(1, 4)
    ))
    while True :
        countries = display_country_table()
        console.print("\n[bold cyan]Enter a county number (or Q to quit):[/bold cyan]")
        choice = input("  > ").strip().upper()
        if choice == "Q":
            console.print("\n[bold green]Thank you for exploring Africa! Goodbye! [/bold green]\n")
        if not validate(choice, len(countries)):
            console.print("[bold red]  Invalid choice. Enter a number between 1 and 54.[/bold red]\n")
            continue
        name, flag, _ = countries[int(choice)-1]
        console.print(Panel(f"{flag}  {name}  selected!", border_style="cyan", padding=(0,2)))
        while True :
            display_menu(f"Exploring {flag} {name} -- Choose a category", [v["label"] for v in CATEGORIES.values()])
            console.print("\n[bold cyan]Enter your choice:[/bold cyan]")
            cat = input("  > ").strip().upper()
            if cat == "Q":
                console.print("\n[bold green]Goodbye! [/bold green]\n")
                sys.exit()
            if cat == "B":
                break
            if cat not in CATEGORIES:
                console.print("[bold red]  Invalid choice.[/bold red]\n")
                continue
            console.print(f"you picked: {CATEGORIES[cat]['label']}")
            while True :
                subs = CATEGORIES[cat]["subs"]
                cat_label = CATEGORIES[cat]["label"]
                display_menu(f"{flag} {name}    {cat_label}", subs, border="magenta")
                console.print("\n[bold cyan]Enter your choice:[/bold cyan]\n")
                sub = input("  > ").strip().upper()
                if sub == "Q" :
                    console.print("\n[bold green]Goodbye! [/bold green]\n")
                    sys.exit()
                if sub == "B":
                    break
                if not validate(sub, len(subs)):
                    console.print("[bold red]  Invalid choice.[/bold red]\n")
                    continue
                selected_sub = subs[int(sub)-1]
                console.print(Panel(f"Generating: {selected_sub}...", border_style="yellow"))
                p= prompt(name, CATEGORIES[cat]["key"], selected_sub)
                content = ai_response(p)
                console.print(Panel(
                    Text(format_response(content)),
                    title=f"{name}    {cat_label}    {selected_sub}",
                    border_style="green",
                    padding=(1, 3),
                ))
                console.print("[dim]Press Enter to continue...[/dim]")
                input()


if __name__ == "__main__":
    main()
