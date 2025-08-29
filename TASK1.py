import matplotlib.pyplot as plt
age_groups = ['0-20 Years', '21-64 Years', '65+ Years']
population = [512, 807, 98]   # in millions
percentage = [36.1, 57.0, 6.9]

plt.figure(figsize=(8,6))
bars = plt.bar(age_groups, population, color=['yellow','blue','magenta'])
for bar, pop, perc in zip(bars, population, percentage):
    plt.text(bar.get_x() + bar.get_width()/2, 
             bar.get_height() + 10, 
             f"{pop}M\n{perc}%", 
             ha='center', fontsize=10, fontweight='bold')

plt.title("India's Population Distribution by Age (2022)", fontsize=14, fontweight='bold')
plt.ylabel("Population (in millions)")
plt.xlabel("Age Groups")

plt.show()
