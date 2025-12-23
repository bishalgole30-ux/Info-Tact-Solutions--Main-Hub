import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_simple_er():
    # 1. Setup the canvas
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    
    
    ec = 'black'

    
    ax.add_patch(patches.Rectangle((4, 3.5), 3, 4, fill=False, edgecolor=ec, lw=2))
    plt.text(5.5, 7.2, 'Fact_Sales', weight='bold', ha='center')
    plt.text(4.2, 6.5, 'Invoice (PK)\nCustomer ID (FK)\nStockCode (FK)\nTotal\nQuantity\nInvoiceDate', va='top')

    ax.add_patch(patches.Rectangle((0.5, 5), 2.5, 2, fill=False, edgecolor=ec))
    plt.text(1.75, 6.7, 'Dim_Customer', weight='bold', ha='center')
    plt.text(0.7, 6.2, 'Customer ID (PK)\nCountry', va='top')

    ax.add_patch(patches.Rectangle((7.5, 5), 2, 2, fill=False, edgecolor=ec))
    plt.text(8.5, 6.7, 'Dim_Product', weight='bold', ha='center')
    plt.text(7.7, 6.2, 'StockCode (PK)\nDescription', va='top')
    plt.plot([3, 4], [6, 6], color='black') 
    plt.text(3.5, 6.2, '1:N', ha='center')

    plt.plot([7, 7.5], [6, 6], color='black')
    plt.text(7.25, 6.2, '1:N', ha='center')

   
    ax.axis('off')
    plt.title("ER Diagram", fontsize=15)
    
    plt.savefig('er.png', bbox_inches='tight')
    plt.show()

draw_simple_er()