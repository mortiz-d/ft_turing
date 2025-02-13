# COLORS #
GREEN = @echo "\033[0;32m"
BLUE = @echo "\033[0;34m" 
PURPLE = @echo "\033[0;35m"
CYAN = @echo "\033[0;36m"
RESET = "\033[1;0m"

# RESOURCES #
SRCS =	srcs/ft_nm.c \
		srcs/main.c \
		srcs/_64/analisis64.c \
		srcs/_64/sort64.c	\
		srcs/_32/analisis32.c \
		srcs/_32/sort32.c	\
		srcs/debug/debug.c 

# FLAGS #
OBJS_DIR = objetos
OBJS = $(SRCS:srcs/%.c=$(OBJS_DIR)/%.o)

NAME = prueba.ml
FILE = unary_sub.json

LIBFT_A = libft/libft.a
FILE_TEST = ft_nm#tests/ft_strlen.o#objetos/main.o#

CC = gcc

CFLAGS = -std=c99   -Wall -Werror -Wextra

# Instructions #
all:
	ocaml $(NAME) $(FILE) "111-11="

clean:

fclean: clean	

re: fclean all

test: re
	clear
	./$(NAME) -a $(FILE_TEST)

.PHONY: all clean fclean re test





