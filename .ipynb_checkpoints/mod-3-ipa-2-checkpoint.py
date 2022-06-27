'''Module 3: Individual Programming Assignment 2

Business Simulations

This assignment covers your ability to apply Python to solve a
    quantitative problem.
'''

def optimal_diet(
    corn_protein_composition, corn_fiber_composition, corn_cost_per_pound,
    soymeal_protein_composition, soymeal_fiber_composition, soymeal_cost_per_pound
):
    '''Optimal Diet.
    20 points.

    You are a consultant for an industrial farm. You were assigned to
        develop the most cost-effective way to feed farm animals
        using a combination of corn and soymeal.

    Your client tells you these facts about the problem:
    1. The blend you develop must be at least 30% protein and at most 5% fiber.
    2. The farm uses at least 800 pounds of feed daily.

    Parameters
    ----------
    corn_protein_composition: float
        the pounds of protein per pound of corn (e.g., 0.09 to represent 9%)
    corn_fiber_composition: float
        the pounds of fiber per pound of corn (e.g., 0.02 to represent 2%)
    corn_cost_per_pound: int
        the dollar cost of 1 pound of corn
    soymeal_protein_composition: float
        the pounds of protein per pound of soymeal (e.g., 0.09 to represent 9%)
    soymeal_fiber_composition: float
        the pounds of fiber per pound of soymeal (e.g., 0.02 to represent 2%)
    soymeal_cost_per_pound: int
        the dollar cost of 1 pound of soymeal

    Returns
    -------
    tuple
        a 2-element tuple of ints representing how many pounds of 
        (corn, soymeal) to add to the mix each day
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    minCostIncurred = 0
    optimalCorn = 0
    optimalSoy = 0
    
    for c in range(801):
        s = 800 - c
        proteinComposition = (c*corn_protein_composition + s*soymeal_protein_composition) / (c+s)
        fiberComposition = (c*corn_fiber_composition + s*soymeal_fiber_composition) / (c+s)
        cost = c*corn_cost_per_pound + s*soymeal_cost_per_pound
            
        if proteinComposition <= 0.3 or fiberComposition >= 0.05:
            continue
        else:
            if optimalCorn == 0 and optimalSoy == 0:
                optimalCorn = c
                optimalSoy = s
                minCostIncurred = cost
            elif cost <= minCostIncurred:
                optimalCorn = c
                optimalSoy = s
                minCostIncurred = cost
            else:
                continue
    
    return (optimalCorn, optimalSoy)

def optimal_investments(
    personal_loan_rate, personal_loan_writeoff_ratio,
    car_loan_rate, car_loan_writeoff_ratio,
    home_loan_rate, home_loan_writeoff_ratio,
    farm_loan_rate, farm_loan_writeoff_ratio,
    commercial_loan_rate, commercial_loan_writeoff_ratio,
    constraint_max_pesos
):
    '''Optimal Investments.
    30 points.

    You are an analyst for a bank. You were assigned to the loans department
        of the bank. This department makes money for the bank by loaning
        depositors' money and earning interest on those loans.
    You were asked to devise an optimal loan allocation. Your boss will not be
        satisfied with the model alone. They want concrete answers.
    Normally, someone might solve this with operations research. However, you know
        Python, and you are willing to try another solution.

    Your supervisor tells you these facts about the problem:
    1. There are five types of loans: personal, car, home, farm, and commercial.
    2. Each type of loan has its own interest rate. 
    3. Each type of loan has its own rate of "bad debts" which cannot be reclaimed.
    4. The bank is constrained by competitive forces to allocate at least 40% of its
        funds to farm and commercial loans combined.
    5. To develop the housing industry, the bank's regulator requires that home
        loans make up at least 50% of the combined total of home, personal, and car loans.
    6. Bank policy is to constrain the total proportion of bad debt to at or below 4%.

    Parameters
    ----------
    personal_loan_rate: float
        the interest rate applied to good (i.e., not bad) debt for personal loans
    personal_loan_writeoff_ratio: float
        the proportion of total money allocated to personal loans that will not accrue interest
    car_loan_rate: float
        the interest rate applied to good (i.e., not bad) debt for car loans
    car_loan_writeoff_ratio: float
        the proportion of total money allocated to car loans that will not accrue interest
    home_loan_rate: float
        the interest rate applied to good (i.e., not bad) debt for home loans
    home_loan_writeoff_ratio: float
        the proportion of total money allocated to home loans that will not accrue interest
    farm_loan_rate: float
        the interest rate applied to good (i.e., not bad) debt for farm loans
    farm_loan_writeoff_ratio: float
        the proportion of total money allocated to farm loans that will not accrue interest
    commercial_loan_rate: float
        the interest rate applied to good (i.e., not bad) debt for commercial loans
    commercial_loan_writeoff_ratio: float
        the proportion of total money allocated to commercial loans that will not accrue interest
    constraint_max_pesos: int
        the total number of pesos available to be allocated to different types of loans

    Returns
    -------
    tuple
        a 5-element tuple of integers representing how many pesos to allocate to
        (personal, car, home, farm, commercial) loans respectively to maximize revenue
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    maxIncome = 0
    optimalInvestments = [0,0,0,0,0] # Personal, Car, Home, Farm, Commercial
    
    for per in range(1,constraint_max_pesos):
        for car in range(1,constraint_max_pesos):
            for home in range(1,constraint_max_pesos):
                for farm in range(1,constraint_max_pesos):
                    for comm in range(1,constraint_max_pesos):
                        
                        totalInvestment = per + car + home + farm + comm
                        farmCommRatio = farm + comm / totalInvestment
                        homeRatio = home / (home + per + car)
                        badRatio = (per*personal_loan_writeoff_ratio + car*car_loan_writeoff_ratio + home*home_loan_writeoff_ratio +\ farm*farm_loan_writeoff_ratio + comm*commercial_loan_writeoff_ratio) / totalInvestment
                        investmentIncome = per*(1 - personal_loan_writeoff_ratio) + car*(1 - car_loan_writeoff_ratio) + home*(1 -\ home_loan_writeoff_ratio) + farm*(1 - farm_loan_writeoff_ratio) + comm*(1 - commercial_loan_writeoff_ratio)
                        
                        if totalInvestment > constraint_max_pesos:
                            continue
                        elif farmCommRatio < 40:
                            continue
                        elif homeRatio < 50:
                            continue
                        elif badRatio > 0.04:
                            continue
                        else:
                            if optimalInvestments[0] == 0 and optimalInvestments[1] == 0 and optimalInvestments[2] == 0 and optimalInvestments[3] == 0 and optimalInvestments[4] == 0:
                                optimalInvestments[0] = per
                                optimalInvestments[1] = car
                                optimalInvestments[2] = home
                                optimalInvestments[3] = farm
                                optimalInvestments[4] = comm
                                maxIncome = investmentIncome
                            elif investmentIncome > maxIncome:
                                optimalInvestments[0] = per
                                optimalInvestments[1] = car
                                optimalInvestments[2] = home
                                optimalInvestments[3] = farm
                                optimalInvestments[4] = comm
                                maxIncome = investmentIncome
                            else:
                                continue
    
    return (optimalInvestments[0],optimalInvestments[1],optimalInvestments[2],optimalInvestments[3],optimalInvestments[4])
