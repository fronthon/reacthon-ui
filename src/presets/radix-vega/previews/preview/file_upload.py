from button import Button
from card import Card, CardContent, CardDescription, CardHeader, CardTitle
from empty import Empty, EmptyContent, EmptyDescription, EmptyHeader, EmptyMedia, EmptyTitle

__js__ = {"lucide-react": ["UploadCloudIcon"]}


def FileUpload():
    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>File Upload</{CardTitle}>
                <{CardDescription}>Drag and drop or browse</{CardDescription}>
            </{CardHeader}>
            <{CardContent}>
                <{Empty} class="border">
                    <{EmptyHeader}>
                        <{EmptyMedia} variant="icon">
                            <{UploadCloudIcon} />
                        </{EmptyMedia}>
                        <{EmptyTitle}>Upload files</{EmptyTitle}>
                        <{EmptyDescription}>PNG, JPG, PDF up to 10MB</{EmptyDescription}>
                    </{EmptyHeader}>
                    <{EmptyContent}>
                        <{Button}>Browse Files</{Button}>
                    </{EmptyContent}>
                </{Empty}>
            </{CardContent}>
        </{Card}>
    """
