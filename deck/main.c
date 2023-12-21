// i single-filed this for the sake of simplicity
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

// known windows issue: sometimes a card number of 0 will be printed

// Constants that define the size of the deck, the number of players, and the size of each player's hand
#define DECK_SIZE 52
#define NUM_PLAYERS 2
#define HAND_SIZE 5

// this is a type - it defines a new data type called Card
typedef struct
{
  char suit;
  int value;
} Card;

// this will populate the deck, adding the 52 cards to the array
void populateDeck(Card *deck)
{
  int index = 0;
  char suits[] = {'H', 'D', 'C', 'S'};
  for (int i = 0; i < 4; i++)
  {
    for (int j = 1; j <= 13; j++)
    {
      // account for aces, jacks, queens, and kings
      char str = ""; // string to hold the card value
      if (j == 1)
      {
        char *str = "A";
      }
      else if (j == 11)
      {
        char *str = "J";
      }
      else if (j == 12)
      {
        char *str = "Q";
      }
      else if (j == 13)
      {
        char *str = "K";
      }
      else
      {
        // convert j to char
        str = j;
      }

      deck[index].suit = suits[i];
      deck[index].value = str;
      index++;
    }
  }
}

// this shuffles the deck - it's a modified version of the Fisher-Yates shuffle https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
void shuffleDeck(Card *deck)
{
  srand(time(NULL));
  for (int i = DECK_SIZE - 1; i > 0; i--)
  {
    int j = rand() % (i + 1);
    Card temp = deck[i];
    deck[i] = deck[j];
    deck[j] = temp;
  }
}

// this deals the cards to each player
void dealCards(Card *deck, Card **hands)
{
  for (int i = 0; i < NUM_PLAYERS; i++)
  {
    for (int j = 0; j < HAND_SIZE; j++)
    {
      hands[i][j] = deck[i * HAND_SIZE + j];
    }
  }
}

// this is the main function
int main()
{
  Card deck[DECK_SIZE];
  Card *hands[NUM_PLAYERS];

  for (int i = 0; i < NUM_PLAYERS; i++)
  {
    hands[i] = malloc(HAND_SIZE * sizeof(Card));
  }

  populateDeck(deck);
  shuffleDeck(deck);
  dealCards(deck, hands);

  // Print the hands of each player
  for (int i = 0; i < NUM_PLAYERS; i++)
  {
    printf("Player %d's hand:\n", i + 1);
    for (int j = 0; j < HAND_SIZE; j++)
    {
      printf("%c%d ", hands[i][j].suit, hands[i][j].value);
    }
    printf("\n");
  }

  // Free memory
  for (int i = 0; i < NUM_PLAYERS; i++)
  {
    free(hands[i]);
  }

  return 0;
}