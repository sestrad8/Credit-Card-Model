# Developer    : Ivana Donevska
# Date         : 2016-01-20
# Program Name : Customer DataGenerator
# Version#     : 5
# Description  : Code that generates customer data
# -----------------------------------------------------------------------------
# History  | ddmmyyyy  |  User     |                Changes
#          | 01192016  | Ivana D.  | Credit Card model,code, ref lists, etc...
#	 01202016  | Jeff K.   | Comments, ref lists, etc...
#	 01202016  | Justin S   | SSN distinct list
# -----------------------------------------------------------------------------*/
# Reference data is located on the test-bmohb console gs://newccdatav3

import csv
import random
from datetime import datetime
from random import randrange

import re
from barnum import gen_data
from constants.constants import (EXCHANGE_CURRENCY, FOREIGN_FINANCIAL_INSTITUTION, FOREIGN_GOVT,
                                 FOREIGN_NONBANK_FINANCIAL_INSTITUTION, INTERNET_GAMBLING, MEDICAL_MARIJUANA_DISPENSARY,
                                 MONEY_SERVICE_BUSINESS,
                                 NONREGULATED_FINANCIAL_INSTITUTION, NOT_PROFIT, PRIVATE_ATM_OPERATOR,
                                 SALES_USED_VEHICLES, THIRD_PARTY_PAYMENT_PROCESSOR, TRANSACTING_PROVIDER)
from constants.constants import (SEG_MODEL_TYPE, MODEL_ID, SEG_MODEL_NAME, SEG_MODEL_SCORE, SEG_MODEL_GROUP,
                                 SEG_MODEL_DESCRIPTION)
from constants.constants import USE_CASE
from data import NAICS
from data import geo_data
from data import zips
from faker import Faker
from utils.weighted import weighted_options

# Dictionary for Account list set to blank
acct_list = []
# Dictionary for CreditCard list set to blank
credit_cards = []
# Dictionary for random Wolfsberg scenario

fake = Faker()


# Creates CSV


def get_file(fn, mode='w'):
    pass


def generate_customers():
    with open('uber_cust.csv', 'w') as f1:
        # Writer for CSV...Pipe delimited...Return for a new line
        writer = csv.writer(f1, delimiter='|', lineterminator='\n', )
        # Header Row
        writer.writerow(
            ['ROWNUM'] + ['accountNumber'] + ['accountCategory'] + ['accountType'] + ['NUM_CCS'] + ['NAME'] + [
                'M_NAME'] + [
                'SSN'] + [
                'AUTHORIZED_NAME2'] + ['M_NAME2'] + ['SSN2'] + \
            ['AUTHORIZED_NAME3'] + ['M_NAME3'] + ['SSN3'] + ['AUTHORIZED_NAME4'] + ['M_NAME4'] + ['SSN4'] + [
                'CREDITCARDNUMBER'] + ['CREDITCARDTYPE'] + ['EMPLOYER'] + ['CUSTEMAIL'] + \
            ['OCCUPATION'] + ['CITY'] + ['STATE'] + ['ZIP'] + ['COUNTRY'] + ['PREVIOUS_CITY'] + [
                'PREVIOUS_STATE'] + \
            ['PREVIOUS_ZIP'] + ['PREVIOUS_COUNTRY'] + ['DOB'] + ['PEP'] + ['SAR'] + ['CLOSEDACCOUNT'] + [
                'RELATED_ACCT'] + ['RELATED_TYPE'] + ['PARTY_TYPE'] + ['PARTY_RELATION'] + [
                'PARTY_STARTDATE'] + ['PARTY_ENDDATE'] + \
            ['LARGE_CASH_EXEMPT'] + ['DEMARKET_FLAG'] + ['DEMARKET_DATE'] + ['PROB_DEFAULT_RISKR'] + [
                'OFFICIAL_LANG_PREF'] + ['CONSENT_SHARING'] + \
            ['PREFERRED_CHANNEL'] + ['PRIMARY_BRANCH_NO'] + ['DEPENDANTS_COUNT'] + ['SEG_MODEL_ID'] + [
                'SEG_MODEL_TYPE'] + \
            ['SEG_MODEL_NAME'] + ['SEG_MODEL_GROUP'] + ['SEG_M_GRP_DESC'] + ['SEG_MODEL_SCORE'] + [
                'ARMS_MANUFACTURER'] + ['AUCTION'] + \
            ['CASHINTENSIVE_BUSINESS'] + ['CASINO_GAMBLING'] + ['CHANNEL_ONBOARDING'] + [
                'CHANNEL_ONGOING_TRANSACTIONS'] + ['CLIENT_NET_WORTH'] + \
            ['COMPLEX_HI_VEHICLE'] + ['DEALER_PRECIOUS_METAL'] + ['DIGITAL_PM_OPERATOR'] + [
                'EMBASSY_CONSULATE'] + ['EXCHANGE_CURRENCY'] + \
            ['FOREIGN_FINANCIAL_INSTITUTION'] + ['FOREIGN_GOVERNMENT'] + [
                'FOREIGN_NONBANK_FINANCIAL_INSTITUTION'] + ['INTERNET_GAMBLING'] + \
            ['MEDICAL_MARIJUANA_DISPENSARY'] + ['MONEY_SERVICE_BUSINESS'] + ['NAICS_CODE'] + [
                'NONREGULATED_FINANCIAL_INSTITUTION'] + \
            ['NOT_PROFIT'] + ['PRIVATELY_ATM_OPERATOR'] + ['PRODUCTS'] + ['SALES_USED_VEHICLES'] + [
                'SERVICES'] + \
            ['SIC_CODE'] + ['STOCK_MARKET_LISTING'] + ['THIRD_PARTY_PAYMENT_PROCESSOR'] + [
                'TRANSACTING_PROVIDER'] + ['HIGH_NET_WORTH'] + ['HIGH_RISK'] + ['RISK_RATING'] + [
                'USE_CASE_SCENARIO'])
        # Loop for number of accounts to generate
        start = 10
        acct_list = []
        # JS - Update code 1/26/2016
        # JS - Create list of SSNs up to 20M and use that to pull from
        liSSNMaster = []
        for i in xrange(30):
            liSSNMaster.append(''.join(str(random.randint(0, 9)) for _ in xrange(9)))
        # JS - Only create as many records as the SSN list has available
        # JS - Use xrange instead of range to minimize memory allocation
        liSSNMaster = list(set(liSSNMaster))
        if len(liSSNMaster) < 30:
            liSSNMaster = []
            for i in xrange(30):
                liSSNMaster.append(''.join(str(random.randint(0, 9)) for _ in xrange(9)))
            liSSNMaster = list(set(liSSNMaster))
        for i in xrange(30):
            # Initiate High Risk Flags
            # Politically Exposed Person
            PEP = 'No'
            # Customer with a Suspicous Activity Report
            SAR = 'No'
            # Customer with a closed account
            Clsd = 'No'
            # High risk customer flag
            high_risk = 'No'
            # High Risk Rating
            hr_rating = ''
            # Customer that was demarketed by the bank
            demarket = 'No'
            dem_date = ''
            # generate closed acct flag
            if max((randrange(0, 98, 1) - 96), 0) == 1:
                Clsd = 'Yes'

            # Random number generator for account number
            # acct = randrange(100000,100000000,1)
            # Random choice for number of credit cards per account number
            no_ccs = weighted_options('number_cc')
            # while acct_list.count(acct) > 0:
            #	acct = randrange(100000,100000000,1)
            # dt = str(datetime.now())
            # acct=str(i)++re.sub('\W','',dt)
            acct = start + 1 + randrange(1, 10, 1)
            start = acct
            # Randomly generates customer name
            name = fake.name()
            tmp = gen_data.create_name()
            # Adds account number to account dictionary
            acct_list.extend([acct])
            # Creates a new row and adds data elements
            ##      JS - Main Account Holder SSN as current index in master SSN list
            ##		row = [i]+[acct]+[random.choice(acct_type)]+[No_CCs]+[name]+[tmp[0]]+[(str(randrange(101,1000,1))+str(randrange(10,100,1))+str(randrange(1000,10000,1)))]
            row = [i] + [acct] + [weighted_options('acct_type')] + [no_ccs] + [name] + [tmp[0]] + [liSSNMaster[i]]
            # Dictionary for names list set to blank
            names = []
            # Dictionary for Social Security Number list set to blank
            ssn = []
            # Generates Name and SSN for Credit Users
            # Middle Name to reduce name dups
            mdl = []
            for j in range(no_ccs - 1):
                names.insert(j, fake.name())
                tmp2 = gen_data.create_name()
                mdl.insert(j, tmp2[0])
                ##      JS - Pull from SSN Master list
                # ssn.insert(j,(str(randrange(101,1000,1))+str(randrange(10,100,1))+str(randrange(1000,10000,1))))
                randInt = randrange(1, len(liSSNMaster), 1)
                if randInt != i:
                    ssn.insert(j, liSSNMaster[randInt])
                else:
                    ssn.insert(j, liSSNMaster[randInt - 1])

            # Name and SSN is set to blank if less than 4 customers on an account

            for k in range(4 - no_ccs):
                names.insert(no_ccs + k, '')
                ssn.insert(no_ccs + k, '')
                mdl.insert(no_ccs, '')
            # Sets CC_NO to a random credit card number
            CC_NO = gen_data.create_cc_number()

            # Extract CC_Number from the tuple returned by CC_Number...Tuple contains CC Number and Type
            # while credit_cards.count(CC_NO[1][0]) > 0:
            CC_TRANS = CC_NO[1][0]

            dt = str(datetime.now())
            clean = re.sub('\W', '', dt)
            printCC = str(CC_TRANS[-4:]) + str(clean[-12:-3]) + str(randrange(1111, 9999, randrange(1, 10, 1)))
            # str(CC_TRANS[-4:])+str(clean[-12:-2])+str(randrange(1111,9999,randrange(1,10,1)))
            # Add CC_Number to control list to prevent duplicates
            # Add data elements to current csv row
            row.extend([names[0], mdl[0], ssn[0], names[1], mdl[1], ssn[1], names[2], mdl[2], ssn[2], printCC, CC_NO[0],
                        gen_data.create_company_name() + ' ' + tmp[1],
                        gen_data.create_email(), gen_data.create_job_title()])

            # Creates Current Address
            zip = random.choice(zips.zip)
            addr = geo_data.create_city_state_zip[zip]
            # Creates Previous address
            zip2 = random.choice(zips.zip)
            addr2 = geo_data.create_city_state_zip[zip2]

            # Add additional data elements to current csv row
            lrg_cash_ex = weighted_options('yes_no')

            # Condition for SARs and Demarketed Clients
            if Clsd == 'Yes':
                # 1% of closed accounts are demarketed but never had a SAR filed
                if max((randrange(0, 101, 1) - 99), 0) == 1 and SAR == 'No':
                    demarket = 'Yes'
                    dem_date = gen_data.create_date(past=True)
                if max((randrange(0, 11, 1) - 9), 0) == 1 and demarket == 'No':
                    # 10% of closed accounts have SARs
                    SAR = 'Yes'
                    # 90% of closed accounts with SARs are demarketed
                    if max((randrange(0, 11, 1) - 9), 0) == 0:
                        demarket = 'Yes'
                        dem_date = gen_data.create_date(past=True)

            if max((randrange(0, 101, 1) - 99), 0) == 1:
                PEP = 'Yes'

            row.extend([addr[0], addr[1], zip, 'US', addr2[0], addr2[1], zip2, 'US',
                        gen_data.create_birthday(min_age=2, max_age=85), PEP, SAR, Clsd])
            # Start Generating related accounts from account list once 10,000 accounts are generated
            if i > 10000:
                rel = int(random.choice(acct_list)) * max((randrange(0, 10001, 1) - 9999), 0)
                if rel <> 0:
                    row.append(rel)
                    row.append(weighted_options('related_type'))
                else:
                    row.append('')
                    row.append('')
            else:
                row.append('')
                row.append('')

            # Randomly generates account start date
            party_start = gen_data.create_date(past=True)
            # Randomly selects consent option for sharing info
            Consent_Share = weighted_options('yes_no')

            # Add additional data elements to current csv row


            row.extend(
                [weighted_options('party_type'), weighted_options('party_relation'), party_start,
                 gen_data.create_date(past=True),
                 lrg_cash_ex, demarket, dem_date, randrange(0, 100, 1), weighted_options('official_lang')])
            # Add data element preferred methond of contact for yes to share info...if not then blank to current row
            if Consent_Share == 'Yes':
                row.extend(['Yes', weighted_options('preferred_channel')])
            else:
                row.extend(['No', ''])
            # DO NOT USE CUST STATUS BELOW - NOT INTEGRATED WITH CLOSED STATUS! Add additional data elements to current csv row
            row.extend([zip, randrange(0, 5, 1)])

            # Generates Segment ID then adds additional Segment data based on the selection to the current csv row
            Segment_ID = randrange(0, 5, 1) % 5

            if Segment_ID == 0:
                row.extend(
                    [MODEL_ID[0], SEG_MODEL_TYPE[0], SEG_MODEL_NAME[0], SEG_MODEL_GROUP[0], SEG_MODEL_DESCRIPTION[0],
                     SEG_MODEL_SCORE[0]])

            if Segment_ID == 1:
                row.extend(
                    [MODEL_ID[1], SEG_MODEL_TYPE[1], SEG_MODEL_NAME[1], SEG_MODEL_GROUP[1], SEG_MODEL_DESCRIPTION[1],
                     SEG_MODEL_SCORE[1]])

            if Segment_ID == 2:
                row.extend(
                    [MODEL_ID[2], SEG_MODEL_TYPE[2], SEG_MODEL_NAME[2], SEG_MODEL_GROUP[2], SEG_MODEL_DESCRIPTION[2],
                     SEG_MODEL_SCORE[2]])

            if Segment_ID == 3:
                row.extend(
                    [MODEL_ID[3], SEG_MODEL_TYPE[3], SEG_MODEL_NAME[3], SEG_MODEL_GROUP[3], SEG_MODEL_DESCRIPTION[3],
                     SEG_MODEL_SCORE[3]]
                )

            if Segment_ID == 4:
                row.extend(
                    [MODEL_ID[4], SEG_MODEL_TYPE[4], SEG_MODEL_NAME[4], SEG_MODEL_GROUP[4], SEG_MODEL_DESCRIPTION[4],
                     SEG_MODEL_SCORE[4]]
                )

            # Add additional data elements to current csv row
            arms_manufacturer = weighted_options('arms_manufacturers')
            auction = weighted_options('auction')
            cash_intensive_business = weighted_options('cash_intensive_business')
            casino_gambling = weighted_options('casino_gambling')
            chan_ob = weighted_options('channel_onboarding')
            chan_txn = weighted_options('channel_ongoing_txn')

            row.extend([arms_manufacturer, auction, cash_intensive_business, casino_gambling, chan_ob, chan_txn])

            # Randomly select whther customer has a High Net Worth
            high_net_worth_flag = weighted_options('high_net_worth')

            # Randomly Generates customer net worth based on the above flag
            if high_net_worth_flag == 'Yes':
                row.append(max(max((randrange(0, 101, 1) - 99), 0) * randrange(1000000, 25000000, 1),
                               randrange(1000000, 5000000, 1)))
            else:
                flag = weighted_options('low_net')
                if flag == 0:
                    row.append(randrange(-250000, 600000, 1))
                else:
                    if flag == 1:
                        row.append(randrange(149000, 151000, 1))
                    else:
                        row.append(randrange(40000, 50000, 1))
            # Add data elements to current csv row
            hr1 = weighted_options('complex_hi_vehicle')
            hr2 = weighted_options('dealer_precious_metal')
            hr3 = weighted_options('digital_pm_operator')
            hr4 = weighted_options('embassy_consulate')
            hr5 = weighted_options('embassy_consulate')
            hr6 = weighted_options('embassy_consulate')
            hr7 = weighted_options('embassy_consulate')
            hr8 = weighted_options('embassy_consulate')
            hr9 = weighted_options('embassy_consulate')
            hr10 = weighted_options('embassy_consulate')
            hr11 = weighted_options('embassy_consulate')
            hr12 = random.choice(NAICS.NAICS_Code)
            hr13 = weighted_options('embassy_consulate')
            hr14 = weighted_options('embassy_consulate')
            # hr15=random.choice(occupation)
            hr16 = weighted_options('embassy_consulate')
            hr17 = weighted_options('embassy_consulate')
            hr18 = weighted_options('embassy_consulate')
            hr19 = weighted_options('services')
            hr20 = weighted_options('sic_code')
            hr21 = weighted_options('stock_market_listing')
            hr22 = weighted_options('embassy_consulate')
            hr23 = weighted_options('embassy_consulate')

            refrating = ['1', '1', '1', '2', '3', '4', '2', '4', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5',
                         '5']
            if (PEP == 'Yes' or SAR == 'Yes' or lrg_cash_ex == 'Yes' or demarket == 'Yes' or arms_manufacturer == 'Yes'
                or auction == 'Yes' or cash_intensive_business == 'Yes' or casino_gambling == 'Yes' or hr1 == 'Yes' or hr2 == 'Yes' or hr3 == 'Yes' or hr4 == 'Yes' or
                        hr5 == 'Yes' or hr6 == 'Yes' or hr7 == 'Yes' or hr8 == 'Yes' or hr9 == 'Yes' or hr10 == 'Yes' or hr11 == 'Yes' or hr13 == 'Yes' or hr14 == 'Yes' or
                        hr16 == 'Yes' or hr17 == 'Yes' or hr18 == 'Yes' or hr22 == 'Yes' or hr23 == 'Yes' or high_net_worth_flag == 'Yes'):
                high_risk = 'Yes'
                hr_rating = random.choice(refrating)

            if SAR == 'No' and high_risk == 'No':
                if max((randrange(0, 101, 1) - 99), 0) == 1:
                    high_risk = 'Yes'
                    hr_rating = random.choice(refrating)
            if PEP == 'No' and high_risk == 'No':
                if max((randrange(0, 101, 1) - 99), 0) == 1:
                    high_risk = 'Yes'
                    hr_rating = random.choice(refrating)

            if high_risk == 'No':
                if max((randrange(0, 101, 1) - 99), 0) == 1:
                    high_risk = 'Yes'
                    hr_rating = random.choice(refrating)

            row.extend(
                [hr1, hr2, hr3, hr4, hr5, hr6, hr7, hr8, hr9, hr10, hr11, hr12, hr13, hr14, hr16, hr17, hr18, hr19,
                 hr20,
                 hr21, hr22, hr23,
                 high_net_worth_flag, high_risk, hr_rating, random.choice(USE_CASE)])
            # End the current row
            writer.writerow(row)


if __name__ == '__main__':
    generate_customers()
