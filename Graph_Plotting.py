import Climate_API as cli
import matplotlib.pyplot as plt

cli

cli.average_of_monthly_averages
cli.average_of_monthly_averages_rain
cli.months
cli.errors
cli.errors_rain

print(cli.average_of_monthly_averages)
print(type(cli.average_of_monthly_averages))

def drawing_graph():
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Months')
    ax1.set_ylabel('Temperature (°C)', color=color)
    ax1.bar(cli.months, cli.average_of_monthly_averages, yerr=cli.errors, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:blue'
    ax2.set_ylabel('Rainfall (mm)', color=color)
    ax2.errorbar(cli.months, cli.average_of_monthly_averages_rain, yerr=cli.errors_rain, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Average monthly Temperature and Rainfall for: ' + cli.country_input)
    plt.show()


drawing_graph()

