# Pokemon chain - longest sequence without repeating
# Rule: next word must start with last letter of previous

pokemon = [
    "audino","bagon","baltoy","banette","bidoof","braviary","bronzor",
    "carracosta","charmeleon","cresselia","croagunk","darmanitan","deino",
    "emboar","emolga","exeggcute","gabite","girafarig","gulpin","haxorus",
    "heatmor","heatran","ivysaur","jellicent","jumpluff","kangaskhan",
    "kricketune","landorus","ledyba","loudred","lumineon","lunatone",
    "machamp","magnezone","mamoswine","nosepass","petilil","pidgeotto",
    "pikachu","pinsir","poliwrath","poochyena","porygon2","porygonz",
    "registeel","relicanth","remoraid","rufflet","sableye","scolipede",
    "scrafty","seaking","sealeo","silcoon","simisear","snivy","snorlax",
    "spoink","starly","tirtouga","trapinch","treecko","tyrogue",
    "vigoroth","vulpix","wailord","wartortle","whismur","wingull","yamask"
]

def longest_chain(words):
    def dfs(current, remaining):
        best_chain = [current]

        for word in remaining:
            if current[-1] == word[0]:
                new_remaining = remaining.copy()
                new_remaining.remove(word)

                candidate_chain = [current] + dfs(word, new_remaining)

                if len(candidate_chain) > len(best_chain):
                    best_chain = candidate_chain

        return best_chain

    max_chain = []

    for word in words:
        remaining_words = words.copy()
        remaining_words.remove(word)

        chain = dfs(word, remaining_words)

        if len(chain) > len(max_chain):
            max_chain = chain

    return max_chain


# Run
result = longest_chain(pokemon)

print("Longest chain length:", len(result))
print(" -> ".join(result))