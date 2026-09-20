# Brew & Bean Cafe Email Labeling Guide

## Purpose

This guide defines how customer emails for Brew & Bean Cafe should be labeled in the dataset. Every email must receive exactly one of these four labels:

- `order`
- `feedback`
- `support`
- `other`

The goal is to apply the labels consistently and avoid guessing information that is not stated in the email.

## 1. `order`

Use `order` when the customer is trying to place, change, add to, or cancel an order.

### Examples

- "I'd like to order two large cappuccinos."
- "Can I add a blueberry muffin to my order?"
- "I'd like to cancel the coffee order I placed earlier."
- "Can I change my latte from medium to large?"
- "Please prepare four coffees for pickup."

### Label as `order` when

- The customer wants to place a new order.
- The customer wants to add something to an order.
- The customer wants to change an order.
- The customer wants to cancel an order.
- The customer is specifying drinks, food, quantities, sizes, or order preferences.

---

## 2. `feedback`

Use `feedback` when the customer is expressing an opinion, review, compliment, criticism, or general comment about their experience, products, service, or cafe.

### Examples

- "The new caramel latte was fantastic."
- "The staff were very friendly."
- "I really enjoyed the atmosphere."
- "The coffee was slightly bitter today."
- "The service was a little slow, but the drinks were good."

### Label as `feedback` when

- The main purpose is to share an opinion or experience.
- The customer is complimenting the cafe, staff, food, drinks, or service.
- The customer is criticizing or reviewing the cafe, food, drinks, or service.
- The customer is making a general suggestion or comment rather than asking for help with a specific problem.

---

## 3. `support`

Use `support` when the customer is experiencing a problem and is asking Brew & Bean Cafe to help resolve it.

### Examples

- "I was charged twice for my order. Please help."
- "My order arrived with the wrong drink."
- "My refund has not appeared yet."
- "The discount code is not working."
- "I cannot log into my account."

### Label as `support` when

- Something went wrong with an order, payment, account, reward, refund, or online service.
- The customer needs assistance fixing a specific problem.
- The customer reports a missing, incorrect, failed, or delayed service.
- The customer is asking staff to investigate or resolve an issue.

---

## 4. `other`

Use `other` for general questions or messages that do not primarily fit `order`, `feedback`, or `support`.

### Examples

- "What time do you open?"
- "Do you have Wi-Fi?"
- "Where is your cafe located?"
- "Do you offer outdoor seating?"
- "Do you have dairy-free milk options?"

### Label as `other` when

- The customer is asking a general information question.
- The message is about opening hours, location, facilities, menu information, accessibility, or general cafe policies.
- The message does not involve placing/changing an order.
- The message is not primarily feedback.
- The message is not reporting a problem that requires support.

---

## Choosing Between Similar Labels

### Order vs. Support

Use `order` when the customer is requesting an action involving an order.

Use `support` when something has gone wrong and the customer needs help resolving it.

**Order:**
> "Can I change my order from a medium latte to a large one?"

**Support:**
> "I ordered a large latte, but received a medium. Can you help?"

### Feedback vs. Support

Use `feedback` when the customer is mainly sharing an opinion or experience.

Use `support` when the customer is asking the cafe to resolve a specific problem.

**Feedback:**
> "The coffee was a little cold today."

**Support:**
> "My coffee arrived cold. Can I get a replacement?"

### Other vs. Order

Use `other` for general questions about the cafe.

Use `order` when the customer is actually requesting or changing an order.

**Other:**
> "What sizes of coffee do you offer?"

**Order:**
> "I'd like a large cappuccino, please."

## General Rules

1. Assign exactly one label to every email.
2. Use only these four labels: `order`, `feedback`, `support`, and `other`.
3. Focus on the main purpose of the email.
4. Do not invent information that is not stated in the email.
5. When an email clearly describes a problem and asks for help resolving it, use `support`.
6. When an email mainly expresses an opinion or review without requesting a resolution, use `feedback`.
7. When an email requests an order-related action, use `order`.
8. Use `other` for general questions and messages that do not fit the other categories.
