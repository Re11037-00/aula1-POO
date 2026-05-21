class Playlist:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)

    def set_id(self, valor):
        if valor <= 0:
            raise ValueError("ID inválido")
        self.__id = valor

    def set_nome(self, valor): self.__nome = valor

    def set_descricao(self, valor): self.__descricao = valor

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def ToString(self):
        return f"id: {self.__id} | nome: {self.__nome} | descricao: {self.__descricao}"

    def __str__(self):
        return self.ToString()


class Musica:
    def __init__(self, id, titulo, artista, album):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)
    def set_id(self, valor):
        if valor <= 0: raise ValueError("ID inválido")
        self.__id = valor
    def set_titulo(self, valor): self.__titulo = valor
    def set_artista(self, valor): self.__artista = valor
    def set_album(self, valor): self.__album = valor
    def get_id(self): return self.__id
    def get_titulo(self): return self.__titulo
    def get_artista(self): return self.__artista
    def get_album(self): return self.__album
    def ToString(self): return f"id: {self.__id} | titulo: {self.__titulo} | artista: {self.__artista} | album: {self.__album}"
    def __str__(self): return self.ToString()


class PlayListItem:
    def __init__(self, id, id_playlist, id_musica, sequencia):
        self.set_id(id)
        self.set_id_playlist(id_playlist)
        self.set_id_musica(id_musica)
        self.set_sequencia(sequencia)
    def set_id(self, valor):
        if valor <= 0:
            raise ValueError("ID inválido")
        self.__id = valor
    def set_id_playlist(self, valor): self.__id_playlist = valor
    def set_id_musica(self, valor): self.__id_musica = valor
    def set_sequencia(self, valor): self.__sequencia = valor
    def get_id(self): return self.__id
    def get_id_playlist(self): return self.__id_playlist
    def get_id_musica(self): return self.__id_musica
    def get_sequencia(self): return self.__sequencia
    def ToString(self): return f"id: {self.__id} | id_playlist: {self.__id_playlist} | id_musica: {self.__id_musica} | sequencia: {self.__sequencia}"
    def __str__(self): return self.ToString()

class UI:
    playlists = []
    musicas = []
    itens = []

    @staticmethod
    def Main():
        while True:
            opcao = UI.Menu()
            if opcao == 1: UI.inserir_playlist()
            elif opcao == 2: UI.listar_playlists()
            elif opcao == 3: UI.atualizar_playlist()
            elif opcao == 4: UI.excluir_playlist()
            elif opcao == 5: UI.inserir_musica()
            elif opcao == 6: UI.listar_musicas()
            elif opcao == 7: UI.atualizar_musica()
            elif opcao == 8: UI.excluir_musica()
            elif opcao == 9: UI.inserir_item()
            elif opcao == 10: UI.listar_itens()
            elif opcao == 11: UI.atualizar_item()
            elif opcao == 12: UI.excluir_item()
            elif opcao == 13:
                UI.listar_itens_da_playlist()
            elif opcao == 14:
                print("Saindo...")
                break
            else:
                print("Opção inválida.")

    @staticmethod
    def Menu():
        print("1-Inserir playlist 2-Listar playlists 3-Atualizar playlist 4-Excluir playlist")
        print("5-Inserir música 6-Listar músicas 7-Atualizar música 8-Excluir música")
        print("9-Inserir item 10-Listar itens 11-Atualizar item 12-Excluir item")
        print("13-Listar itens de uma playlist 14-Sair")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def inserir_playlist():
        print("Inserir Playlist:")
        id = int(input("Informe o id da playlist: "))
        nome = input("Informe o nome da playlist: ")
        descricao = input("Informe a descricao da playlist: ")
        playlist = Playlist(id, nome, descricao)
        UI.playlists.append(playlist)
        print("Playlist inserida com sucesso!")

    @staticmethod
    def listar_playlists():
        print("Lista de Playlists:")
        if len(UI.playlists) == 0: print("Nenhuma playlist cadastrada.")
        else:
            for playlist in UI.playlists: print(playlist)

    @staticmethod
    def atualizar_playlist():
        print("Atualizar Playlist:")
        id = int(input("Informe o id da playlist a ser atualizada: "))
        playlist = UI.find_playlist(id)
        if playlist is None:
            print("Playlist não encontrada.")
            return
        nome = input("Informe o novo nome da playlist: ")
        descricao = input("Informe a nova descricao da playlist: ")
        playlist.set_nome(nome)
        playlist.set_descricao(descricao)
        print("Playlist atualizada com sucesso!")

    @staticmethod
    def excluir_playlist():
        print("Excluir Playlist:")
        id = int(input("Informe o id da playlist a ser excluída: "))
        playlist = UI.find_playlist(id)
        if playlist is None:
            print("Playlist não encontrada.")
            return
        UI.playlists.remove(playlist)
        UI.itens = [item for item in UI.itens if item.get_id_playlist() != id]
        print("Playlist excluída com sucesso!")

    @staticmethod
    def inserir_musica():
        print("Inserir Música:")
        id = int(input("Informe o id da música: "))
        titulo = input("Informe o titulo da música: ")
        artista = input("Informe o artista da música: ")
        album = input("Informe o album da música: ")
        musica = Musica(id, titulo, artista, album)
        UI.musicas.append(musica)
        print("Música inserida com sucesso!")

    @staticmethod
    def listar_musicas():
        print("Lista de Músicas:")
        if len(UI.musicas) == 0:
            print("Nenhuma música cadastrada.")
        else:
            for musica in UI.musicas:
                print(musica)

    @staticmethod
    def atualizar_musica():
        print("Atualizar Música:")
        id = int(input("Informe o id da música a ser atualizada: "))
        musica = UI.find_musica(id)
        if musica is None:
            print("Música não encontrada.")
            return
        titulo = input("Informe o novo titulo da música: ")
        artista = input("Informe o novo artista da música: ")
        album = input("Informe o novo album da música: ")
        musica.set_titulo(titulo)
        musica.set_artista(artista)
        musica.set_album(album)
        print("Música atualizada com sucesso!")

    @staticmethod
    def excluir_musica():
        print("Excluir Música:")
        id = int(input("Informe o id da música a ser excluída: "))
        musica = UI.find_musica(id)
        if musica is None:
            print("Música não encontrada.")
            return
        UI.musicas.remove(musica)
        UI.itens = [item for item in UI.itens if item.get_id_musica() != id]
        print("Música excluída com sucesso!")

    @staticmethod
    def inserir_item():
        print("Inserir Item de Playlist:")
        id = int(input("Informe o id do item: "))
        id_playlist = int(input("Informe o id da playlist: "))
        id_musica = int(input("Informe o id da música: "))
        sequencia = int(input("Informe a sequencia da música na playlist: "))
        if UI.find_playlist(id_playlist) is None:
            print("Playlist não encontrada.")
            return
        if UI.find_musica(id_musica) is None:
            print("Música não encontrada.")
            return
        item = PlayListItem(id, id_playlist, id_musica, sequencia)
        UI.itens.append(item)
        print("Item inserido com sucesso!")

    @staticmethod
    def listar_itens():
        print("Lista de Itens de Playlist:")
        if len(UI.itens) == 0:
            print("Nenhum item cadastrado.")
        else:
            for item in UI.itens:
                print(item)

    @staticmethod
    def atualizar_item():
        print("Atualizar Item de Playlist:")
        id = int(input("Informe o id do item a ser atualizado: "))
        item = UI.find_item(id)
        if item is None:
            print("Item não encontrado.")
            return
        id_playlist = int(input("Informe o novo id da playlist: "))
        id_musica = int(input("Informe o novo id da música: "))
        sequencia = int(input("Informe a nova sequencia da música na playlist: "))
        if UI.find_playlist(id_playlist) is None:
            print("Playlist não encontrada.")
            return
        if UI.find_musica(id_musica) is None:
            print("Música não encontrada.")
            return
        item.set_id_playlist(id_playlist)
        item.set_id_musica(id_musica)
        item.set_sequencia(sequencia)
        print("Item atualizado com sucesso!")

    @staticmethod
    def excluir_item():
        print("Excluir Item de Playlist:")
        id = int(input("Informe o id do item a ser excluído: "))
        item = UI.find_item(id)
        if item is None:
            print("Item não encontrado.")
            return
        UI.itens.remove(item)
        print("Item excluído com sucesso!")

    @staticmethod
    def listar_itens_da_playlist():
        print("Listar Itens da Playlist:")
        id_playlist = int(input("Informe o id da playlist: "))
        if UI.find_playlist(id_playlist) is None:
            print("Playlist não encontrada.")
            return
        itens_da_playlist = [item for item in UI.itens if item.get_id_playlist() == id_playlist]
        if len(itens_da_playlist) == 0:
            print("Nenhum item encontrado para essa playlist.")
            return
        for item in itens_da_playlist:
            musica = UI.find_musica(item.get_id_musica())
            descricao_musica = musica.get_titulo() if musica is not None else "Música removida"
            print(f"{item} | titulo_musica: {descricao_musica}")

    @staticmethod
    def find_playlist(id_playlist):
        for playlist in UI.playlists:
            if playlist.get_id() == id_playlist:
                return playlist
        return None

    @staticmethod
    def find_musica(id_musica):
        for musica in UI.musicas:
            if musica.get_id() == id_musica:
                return musica
        return None

    @staticmethod
    def find_item(id_item):
        for item in UI.itens:
            if item.get_id() == id_item:
                return item
        return None


UI.Main()
       