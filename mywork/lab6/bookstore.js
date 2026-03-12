// Task 2: use database
use bookstore

// Task 3: insert first author
db.authors.insertOne({
  name: "Jane Austen",
  nationality: "British",
  bio: {
    short: "English novelist known for novels about the British landed gentry.",
    long: "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma, celebrated for their wit, social commentary, and masterful character development."
  }
})

// Task 4: update to add birthday
db.authors.updateOne(
  { name: "Jane Austen" },
  { $set: { birthday: "1775-12-16" } }
)

// Task 5: insert four more authors
db.authors.insertMany([
  {
    name: "George Orwell",
    nationality: "British",
    bio: {
      short: "British writer known for dystopian fiction.",
      long: "George Orwell was an English novelist, essayist, journalist, and critic, best known for Animal Farm and 1984."
    },
    birthday: "1903-06-25"
  },
  {
    name: "Haruki Murakami",
    nationality: "Japanese",
    bio: {
      short: "Japanese novelist known for surreal contemporary fiction.",
      long: "Haruki Murakami is a Japanese writer whose novels blend surrealism, loneliness, and pop culture."
    },
    birthday: "1949-01-12"
  },
  {
    name: "Chinua Achebe",
    nationality: "Nigerian",
    bio: {
      short: "Nigerian novelist known for Things Fall Apart.",
      long: "Chinua Achebe was a Nigerian novelist, poet, and critic whose work explored colonialism and African identity."
    },
    birthday: "1930-11-16"
  },
  {
    name: "Gabriel Garcia Marquez",
    nationality: "Colombian",
    bio: {
      short: "Colombian novelist associated with magical realism.",
      long: "Gabriel Garcia Marquez was a Colombian novelist and Nobel Prize winner, best known for One Hundred Years of Solitude."
    },
    birthday: "1927-03-06"
  }
])

// Task 6: total count
db.authors.countDocuments()

// Task 7: British authors, sorted by name
db.authors.find({ nationality: "British" }).sort({ name: 1 })
