
# let's just knock out a loose map first

# two zones: mushroom forest and the city
    # mushrooms are found in the forest, sold in the city

# player will start looking for easy mushrooms; unmodified roll to find (d20?)
  # (morel/lion's mane/sulphur shelf/maitake/oyster)
# mushrooms can be sold (for money) or eaten (for satiation/insight)
  # satiation slowly drains over time
  # it resets when you go back to town
  # you have to go back to town after a certain number of searches anyway
  # insight gives a bonus to finding mushrooms or possibly extra searches
  # it also resets when you go back to town
  # want to find a balance of eating mushrooms for the bonus and selling for money
# money lets you buy tools
  # (field guide/waterproof boots/chaos the truffle-sniffing dog/??)
  # tools let you stay out longer or find more difficult mushrooms
# more difficult mushrooms require tools + insight to find but give more insight + money
  # what is a more difficult mushroom? quick google is very unhelpful here am i going to have to buy a BOOK!?
# no real end condition, just keep playing till you get rich and find awesome mushrooms
# this is the odell lake of mushroom foraging
# the time limit is your bus drops you off or you get bored

# we need tables for
  # mushroom types, increasing in difficulty of finding/value
  # tools, increasing in potency/price

# we need objects for
  # the player character, has properties:
    # current insight (int)
    # current remaining rolls (int)
    # current mushroom inventory (array)
    # current money (int)
    # current tools (array?)

# we need functions for
  # user input (look for mushrooms, eat or save, go back to town, sell or buy)
    # is mushroom success entirely contingent on buffs with a single roll and target DCs, or
    # can the user intentionally look for different tiers?
  # random mushroom success roll
    # takes as input player object (insight, #rolls remaining, tools)
    # once mushroom is picked up, prompt player for use/eat
  # use/eat mushroom
    # modifies player object. might want to take as input just to future-proof
  # item purchase
    # takes as input player object (money, tools), tools table
  # mushroom sale
    # takes as input player object (money, inventory), mushroom table

# it would be nice if
  # chaos reacts to you and your successes (why have a dog if you cannot PET HER)
  # bad mushrooms are an option at higher levels, can cost money/end trip
    # this would be a good reason to make difficulty bands targetable; choose to
    # make slow low-level profits or riskier faster at a higher tier
  