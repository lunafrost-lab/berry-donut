class PaginationManager:
    def __init__(self, page_size=50):
        self.page_size = page_size
        self.current_page = 1
        self.total_rows = 0
        self.total_pages = 1

    def update(self, total_rows):
        self.total_rows = total_rows
        self.total_pages = max(1, (self.total_rows + self.page_size - 1) // self.page_size)
        self.current_page = 1

    def offset_limit(self):
        offset = (self.current_page - 1) * self.page_size
        return offset, self.page_size

    def can_prev(self):
        return self.current_page > 1

    def can_next(self):
        return self.current_page < self.total_pages

    def goto_first(self): self.current_page = 1
    def goto_last(self): self.current_page = self.total_pages
    def prev_page(self): self.current_page = max(1, self.current_page - 1)
    def next_page(self): self.current_page = min(self.total_pages, self.current_page + 1)
