#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define DECK_SIZE 52
#define NUM_PLAYERS 2
#define HAND_SIZE 5

typedef struct
{
  char suit;
  int value;
} Card;

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