import seaborn as sns
Solar_perc = data.groupby("Image_id").target.value_counts()/ data.groupby("Image_id").target.size()
Solar_perc = Solar_perc.unstack()

fig, ax = plt.subplots(1,3,figsize=(25,5))

# Plotting Frequency of Patches per City
sns.distplot(data.groupby("Image_id").size(), ax=ax[0], color="Orange", kde=False, bins=15)
ax[0].set_xlabel("Number of solar")
ax[0].set_ylabel("Frequency")
ax[0].set_title("How many solar  do we have per City?")

# Plotting Percentage of an image that is covered by Solar
sns.distplot(Solar_perc.loc[:, 1]*100, ax=ax[1], color="Tomato", kde=False, bins=15)
ax[1].set_title("How much percentage of an image is covered?")
ax[1].set_ylabel("Frequency")
ax[1].set_xlabel("% of solar with Solar")

# Plotting number of patches that show Solar
sns.countplot(data.target, palette='pastel', ax=ax[2]);
ax[2].set_ylabel("Count")
ax[2].set_xlabel("no(0) versus yes(1)")
ax[2].set_title("How many solar show?");
