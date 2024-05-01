def savings(gross_pay, tax_rate, expenses):
    """Calculate the money remaining for an employee after taxes and expenses.

    Parameters
    ----------
    gross_pay : int
        The gross pay of an employee for a certain time period, expressed in centavos.
    tax_rate : float
        The tax rate for a certain time period, expressed as a number between 0 and 1.
    expenses : int
        The expenses of an employee for a certain time period, expressed in centavos.

    Returns
    -------
    int
        The number of centavos remaining from an employee's pay after taxes and expenses.
    """
    tax_amount = int(gross_pay * tax_rate)
    after_tax_pay = gross_pay - tax_amount
    remaining = after_tax_pay - expenses
    return remaining

def material_waste(total_material, material_units, num_jobs, job_consumption):
    """Calculate how much material input will be wasted after running a certain number of jobs.

    Parameters
    ----------
    total_material : int
        The total material available.
    material_units : str
        The units used to express a quantity of the material.
    num_jobs : int
        The number of jobs to run.
    job_consumption : int
        The amount of material consumed per job.

    Returns
    -------
    str
        The amount of remaining material expressed with its unit.
    """
    total_consumption = num_jobs * job_consumption
    remaining_material = total_material - total_consumption
    return f"{remaining_material}{material_units}"

def interest(principal, rate, periods):
    """Calculate the final value of an investment after gaining simple interest over a number of periods.

    Parameters
    ----------
    principal : int
        The principal (starting) amount invested, expressed in centavos.
    rate : float
        The interest rate per period, expressed as a decimal representation of a percentage.
    periods : int
        The number of periods invested.

    Returns
    -------
    int
        The final value of the investment.
    """
    interest_amount = int(principal * rate * periods)
    final_value = principal + interest_amount
    return final_value
