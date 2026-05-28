import helpers

def main():
    counts = {}
    words = get_words("2025 canadian federal election results.txt")
    lowercase_words = [world.lower() for word in words if len(word) > 4]
    
    
    counts = {word: words.count(word) for word in lowercase_words}

    save_counts(counts)

main()

