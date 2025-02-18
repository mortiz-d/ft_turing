# # COLORS #
# GREEN = @echo "\033[0;32m"
# BLUE = @echo "\033[0;34m" 
# PURPLE = @echo "\033[0;35m"
# CYAN = @echo "\033[0;36m"
# RESET = "\033[1;0m"

# # RESOURCES #
# SRCS =	srcs/prueba.ml \
# 		srcs/get_next_line.ml

# # FLAGS #
# OBJS_DIR = objetos
# OBJS = $(SRCS:srcs/%.c=$(OBJS_DIR)/%.o)

# NAME = srcs/prueba.ml
# FILE = unary_sub.json

# LIBFT_A = libft/libft.a
# FILE_TEST = ft_nm#tests/ft_strlen.o#objetos/main.o#

# CC = gcc

# CFLAGS = -std=c99   -Wall -Werror -Wextra

# # Instructions #
# all:
# 	ocamlc -c archivo1.mli archivo1.ml 
# 	ocaml $(SRCS) $(FILE) "111-11="

# clean:

# fclean: clean	

# re: fclean all

# test: re
# 	clear
# 	./$(NAME) -a $(FILE_TEST)

# .PHONY: all clean fclean re test



# COLORS #
GREEN = @echo "\033[0;32m"
BLUE = @echo "\033[0;34m" 
PURPLE = @echo "\033[0;35m"
CYAN = @echo "\033[0;36m"
RESET = "\033[1;0m"

# RESOURCES #
SRCS =	\
		srcs/get_next_line.ml\
		srcs/prueba.ml 

# FLAGS #
OBJS_DIR = objetos
OBJS = $(SRCS:srcs/%.ml=$(OBJS_DIR)/%.mli)

NAME = ft_nm

LIBFT_A = libft/libft.a

# COMPILING
CC = ocamlc

CFLAGS = 

# Instructions #
all: $(NAME)

$(NAME): $(OBJS)
	@make -C ./libft
	$(CC) $(CFLAGS) -o $(NAME) $(OBJS)
	export LC_COLLATE=C
	$(BLUE) NM set Up $(RESET)

$(OBJS_DIR)/%.mli: srcs/%.ml
#Creamos las carpetas necesarias para compilar
	@mkdir -p $(dir $@)
	@echo $(BLUE) Hola $(RESET)
	$(CC) -c $<   $@
	$(CYAN) NM Object Compiled $< $(RESET)

clean:
	@make fclean -s -C./libft
	@rm -rf $(OBJS_DIR)
	@rm -rf $(TEST)
	$(PURPLE) Cleaned NM Objects $(RESET)

fclean: clean
	rm -rf $(NAME)
	$(PURPLE) Cleaned NM Executable $(RESET)	

re: fclean all

.PHONY: all clean fclean re test debug



