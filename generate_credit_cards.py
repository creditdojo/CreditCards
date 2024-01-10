import json
import uuid

def generate_credit_cards(name, issuer, points_type, rewards, fee, credits, benefits):
  """
  In: 
  name: Str -> name of credit card, without issuer name
  issuer: Str -> name of credit card issuer (i.e. bank)
  points_type: Str -> [cashback, travel]
  rewards: {Str: Float} -> earning rates in each category
  fee: Int -> annual fee of the card
  credits: {Obj} -> each type of credit, frequency of issue, etc.
  benefits: [Str] -> list of benefits with no explicit cash value

  Out:
  JSON object with fields and values as defined
  """
  entry = {
    "uuid": str(uuid.uuid4()),
    "name": name,
    "issue": issuer,
    "points_type": points_type,
    "rewards": rewards,
    "fee": fee,
    "credits": credits,
    "benefits": benefits
  }

  return entry

# example
wells_fargo_active_cash = {
    "uuid": "absdajnd-12345"
    "name": "Active Cash",
    "issue": "Wells Fargo",
    "points_type": "cashback",
    "rewards": {
      "other": 2
    },
    "fee": 0,
    "credits": {},
    "benefits": []
}

wfac_rewards = {"other": 2}
wfac_credits = {}
wfac_benefits = []

def main():
  # representative examples of credit cards here
  # Wells Fargo Active Cash - 2% back on everything
  # CapitalOne SavorOne - multiple different rewards cateogries
  # American Express Blue Cash Preferred - multiple rewards, fee
  # Citi Prestige - multiple rewards, fee, single credit
  # American Express Gold - multiple rewards, fee, monhtly credits
  # American Express Platinum - multiple rewards, fee, various credits + benefits
  credit_cards = [
    generate_credit_cards("Active Cash", "Wells Fargo", "cashback", )
  ]